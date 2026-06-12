from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase

from .access import (
    ADMIN,
    EMPLOYEE,
    MANAGER,
    RoleBasedPermission,
    RoleScopedViewSetMixin,
    get_user_profile,
)
from .auth import UserAccountAuthToken


class RoleBasedPermissionTests(SimpleTestCase):
    @patch('useraccounts.access.get_user_account')
    def test_business_profile_overrides_django_superuser_flag(self, get_account):
        get_account.return_value = SimpleNamespace(profile=MANAGER)
        user = SimpleNamespace(is_superuser=True)

        self.assertEqual(get_user_profile(user), MANAGER)

    @patch('useraccounts.access.get_user_profile', return_value=MANAGER)
    def test_manager_cannot_update_users(self, _get_profile):
        request = SimpleNamespace(user=SimpleNamespace())
        view = SimpleNamespace(
            action='update',
            manager_allowed_actions=('list', 'retrieve'),
        )

        self.assertFalse(RoleBasedPermission().has_permission(request, view))

    @patch('useraccounts.access.get_user_profile', return_value=EMPLOYEE)
    def test_employee_can_only_use_explicit_read_actions(self, _get_profile):
        request = SimpleNamespace(user=SimpleNamespace())
        view = SimpleNamespace(
            action='list',
            employee_allowed_actions=('list', 'retrieve'),
        )

        self.assertTrue(RoleBasedPermission().has_permission(request, view))

        view.action = 'destroy'
        self.assertFalse(RoleBasedPermission().has_permission(request, view))


class FakeQuerysetView:
    def get_queryset(self):
        return self.queryset


class ScopedTestView(RoleScopedViewSetMixin, FakeQuerysetView):
    employee_filter = 'contract__employee_id'


class RoleScopedViewSetMixinTests(SimpleTestCase):
    @patch('useraccounts.access.get_user_account')
    @patch('useraccounts.access.get_user_profile', return_value=EMPLOYEE)
    def test_employee_queryset_is_filtered_by_linked_employee(
        self,
        _get_profile,
        get_account,
    ):
        queryset = MagicMock()
        scoped = queryset.filter.return_value
        scoped.values.return_value = 'scoped-ids'
        view = ScopedTestView()
        view.queryset = queryset
        view.request = SimpleNamespace(user=SimpleNamespace())
        get_account.return_value = SimpleNamespace(employee_id=42)

        result = view.get_queryset()

        self.assertEqual(queryset.filter.call_count, 2)
        queryset.filter.assert_any_call(contract__employee_id=42)
        scoped.values.assert_called_once_with('pk')
        queryset.filter.assert_any_call(pk__in='scoped-ids')
        self.assertEqual(result, queryset.filter.return_value)


class LoginAuditTests(SimpleTestCase):
    @patch('useraccounts.auth.record_audit_event')
    @patch('useraccounts.auth.set_auth_cookie')
    @patch('useraccounts.auth.Token.objects.get_or_create')
    @patch('useraccounts.auth.get_user_account')
    @patch('useraccounts.auth.authenticate')
    def test_django_login_passes_business_account_to_audit(
        self,
        authenticate,
        get_account,
        get_token,
        _set_cookie,
        record_audit,
    ):
        django_user = SimpleNamespace(username='admin')
        account = SimpleNamespace(profile=ADMIN, employee_id=1)
        authenticate.return_value = django_user
        get_account.return_value = account
        get_token.return_value = (SimpleNamespace(key='token'), False)
        request = SimpleNamespace(data={'username': 'admin', 'password': 'senha'})

        UserAccountAuthToken().post(request)

        record_audit.assert_called_once()
        self.assertIs(record_audit.call_args.kwargs['user_account'], account)
