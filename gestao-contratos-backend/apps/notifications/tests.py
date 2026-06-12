from datetime import date, timedelta
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase

from .services import (
    contract_expiration_key,
    create_contract_expiration_notification,
    create_payment_overdue_notification,
    payment_overdue_key,
)
from .views import NotificationViewSet


class NotificationServiceTests(SimpleTestCase):
    def setUp(self):
        self.today = date(2026, 6, 11)
        self.contract = SimpleNamespace(
            pk=10,
            number='CTR-010',
            end_date=self.today + timedelta(days=30),
            status='ATIVO',
        )

    @patch('notifications.services.Notification.objects.get_or_create')
    def test_contract_expiring_in_thirty_days_creates_notification(self, get_or_create):
        get_or_create.return_value = (SimpleNamespace(), True)

        created = create_contract_expiration_notification(self.contract, self.today)

        self.assertTrue(created)
        get_or_create.assert_called_once()
        self.assertEqual(
            get_or_create.call_args.kwargs['source_key'],
            contract_expiration_key(self.contract),
        )

    @patch('notifications.services.Notification.objects.get_or_create')
    def test_closed_contract_does_not_create_notification(self, get_or_create):
        self.contract.status = 'ENCERRADO'

        created = create_contract_expiration_notification(self.contract, self.today)

        self.assertFalse(created)
        get_or_create.assert_not_called()

    @patch('notifications.services.Notification.objects.get_or_create')
    def test_payment_due_yesterday_creates_notification(self, get_or_create):
        get_or_create.return_value = (SimpleNamespace(), True)
        payment = SimpleNamespace(
            pk=20,
            installment_number=2,
            due_date=self.today - timedelta(days=1),
            status='PENDENTE',
            contract=self.contract,
        )

        created = create_payment_overdue_notification(payment, self.today)

        self.assertTrue(created)
        self.assertEqual(
            get_or_create.call_args.kwargs['source_key'],
            payment_overdue_key(payment),
        )

    @patch('notifications.services.Notification.objects.get_or_create')
    def test_payment_due_today_is_not_overdue(self, get_or_create):
        payment = SimpleNamespace(
            pk=20,
            installment_number=2,
            due_date=self.today,
            status='PENDENTE',
            contract=self.contract,
        )

        created = create_payment_overdue_notification(payment, self.today)

        self.assertFalse(created)
        get_or_create.assert_not_called()

    @patch('notifications.services.Notification.objects.get_or_create')
    def test_dismissed_payment_notification_is_not_recreated(self, get_or_create):
        get_or_create.return_value = (
            SimpleNamespace(is_dismissed=1),
            False,
        )
        payment = SimpleNamespace(
            pk=20,
            installment_number=2,
            due_date=self.today - timedelta(days=1),
            status='PENDENTE',
            contract=self.contract,
        )

        created = create_payment_overdue_notification(payment, self.today)

        self.assertFalse(created)
        get_or_create.assert_called_once()


class NotificationViewSetTests(SimpleTestCase):
    def test_mark_read_updates_unread_notification(self):
        notification = MagicMock(is_read=False)
        view = NotificationViewSet()
        view.get_object = MagicMock(return_value=notification)
        view.get_serializer = MagicMock(
            return_value=SimpleNamespace(data={'id': 1, 'is_read': True})
        )

        response = view.mark_read(request=None)

        self.assertTrue(notification.is_read)
        notification.save.assert_called_once_with(update_fields=['is_read'])
        self.assertEqual(response.data['is_read'], True)

    def test_mark_read_does_not_save_notification_twice(self):
        notification = MagicMock(is_read=True)
        view = NotificationViewSet()
        view.get_object = MagicMock(return_value=notification)
        view.get_serializer = MagicMock(
            return_value=SimpleNamespace(data={'id': 1, 'is_read': True})
        )

        view.mark_read(request=None)

        notification.save.assert_not_called()

    @patch('notifications.views.record_audit_event')
    def test_destroy_dismisses_automatic_notification(self, record_audit_event):
        notification = MagicMock(source_key='payment-overdue:20:2026-06-10')
        notification.is_dismissed = 0
        view = NotificationViewSet()
        view.request = SimpleNamespace()
        view.get_audit_description = MagicMock(return_value='Notificacao excluida.')

        view.perform_destroy(notification)

        self.assertEqual(notification.is_dismissed, 1)
        notification.save.assert_called_once_with(update_fields=['is_dismissed'])
        record_audit_event.assert_called_once()
