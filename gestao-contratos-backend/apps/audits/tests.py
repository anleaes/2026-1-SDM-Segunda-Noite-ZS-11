from types import SimpleNamespace
from unittest.mock import patch

from django.test import SimpleTestCase

from .services import get_audit_user, get_client_ip, record_audit_event
from .views import AuditViewSet


class AuditServiceTests(SimpleTestCase):
    @patch('audits.services.UserAccount.objects.filter')
    def test_get_audit_user_uses_authenticated_username(self, filter_accounts):
        expected_account = object()
        filter_accounts.return_value.first.return_value = expected_account
        request = SimpleNamespace(user=SimpleNamespace(username='admin'))

        account = get_audit_user(request)

        self.assertIs(account, expected_account)
        filter_accounts.assert_called_once_with(username='admin')

    def test_get_client_ip_uses_first_forwarded_address(self):
        request = SimpleNamespace(META={
            'HTTP_X_FORWARDED_FOR': '203.0.113.10, 10.0.0.1',
            'REMOTE_ADDR': '127.0.0.1',
        })

        self.assertEqual(get_client_ip(request), '203.0.113.10')

    @patch('audits.services.get_audit_user', return_value=None)
    @patch('audits.services.Audit.objects.create')
    def test_record_audit_event_creates_expected_entry(self, create_audit, _get_user):
        request = SimpleNamespace(
            META={'REMOTE_ADDR': '127.0.0.1'},
            user=SimpleNamespace(username='tester'),
        )

        record_audit_event(
            request=request,
            action='CRIACAO',
            description='Registro criado.',
        )

        create_audit.assert_called_once()
        fields = create_audit.call_args.kwargs
        self.assertEqual(fields['action'], 'CRIACAO')
        self.assertEqual(fields['description'], 'Registro criado.')
        self.assertEqual(fields['ip_address'], '127.0.0.1')


class AuditAccessTests(SimpleTestCase):
    def test_only_admin_profile_has_audit_actions(self):
        self.assertEqual(AuditViewSet.manager_allowed_actions, ())
        self.assertEqual(AuditViewSet.employee_allowed_actions, ())
