from datetime import timedelta

from django.utils import timezone

from contracts.models import Contract
from payments.models import Payment

from .models import Notification


CONTRACT_EXPIRATION_WINDOW_DAYS = 30


def contract_expiration_key(contract):
    return f'contract-expiration:{contract.pk}:{contract.end_date.isoformat()}'


def payment_overdue_key(payment):
    return f'payment-overdue:{payment.pk}:{payment.due_date.isoformat()}'


def create_contract_expiration_notification(contract, today=None):
    today = today or timezone.localdate()
    limit_date = today + timedelta(days=CONTRACT_EXPIRATION_WINDOW_DAYS)

    if contract.status in {'CANCELADO', 'ENCERRADO', 'VENCIDO'}:
        return False

    if not today <= contract.end_date <= limit_date:
        return False

    days_remaining = (contract.end_date - today).days
    _, created = Notification.objects.get_or_create(
        source_key=contract_expiration_key(contract),
        defaults={
            'title': 'Contrato proximo do vencimento',
            'message': (
                f'O contrato {contract.number} termina em {days_remaining} '
                f'dia(s), em {contract.end_date.strftime("%d/%m/%Y")}.'
            ),
            'notification_date': today,
            'notification_type': 'VENCIMENTO',
            'contract': contract,
        },
    )
    return created


def create_payment_overdue_notification(payment, today=None):
    today = today or timezone.localdate()

    if payment.status in {'PAGO', 'CANCELADO'} or payment.due_date >= today:
        return False

    days_overdue = (today - payment.due_date).days
    _, created = Notification.objects.get_or_create(
        source_key=payment_overdue_key(payment),
        defaults={
            'title': 'Pagamento atrasado',
            'message': (
                f'A parcela {payment.installment_number} do contrato '
                f'{payment.contract.number} esta atrasada ha {days_overdue} dia(s).'
            ),
            'notification_date': today,
            'notification_type': 'PAGAMENTO',
            'contract': payment.contract,
        },
    )
    return created


def generate_system_notifications(today=None):
    today = today or timezone.localdate()
    limit_date = today + timedelta(days=CONTRACT_EXPIRATION_WINDOW_DAYS)
    created_count = 0

    contracts = Contract.objects.filter(
        end_date__range=(today, limit_date),
    ).exclude(status__in=['CANCELADO', 'ENCERRADO', 'VENCIDO'])

    payments = Payment.objects.select_related('contract').filter(
        due_date__lt=today,
    ).exclude(status__in=['PAGO', 'CANCELADO'])

    for contract in contracts:
        created_count += int(create_contract_expiration_notification(contract, today))

    for payment in payments:
        created_count += int(create_payment_overdue_notification(payment, today))

    return created_count
