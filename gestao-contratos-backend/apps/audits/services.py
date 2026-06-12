import logging

from django.utils import timezone

from contracts.models import Contract
from useraccounts.models import UserAccount

from .models import Audit


logger = logging.getLogger(__name__)


def get_client_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()

    return request.META.get('REMOTE_ADDR') or 'IP nao informado'


def get_related_contract(instance, include_contract=True):
    if instance is None:
        return None

    if include_contract and isinstance(instance, Contract):
        return instance

    return getattr(instance, 'contract', None)


def get_audit_user(request, user_account=None):
    if user_account is not None:
        return user_account

    username = getattr(getattr(request, 'user', None), 'username', None)
    if not username:
        return None

    return UserAccount.objects.filter(username=username).first()


def record_audit_event(
    *,
    request,
    action,
    description,
    instance=None,
    contract=None,
    user_account=None,
):
    try:
        Audit.objects.create(
            action=action,
            description=description[:500],
            action_date=timezone.localdate(),
            ip_address=get_client_ip(request)[:50],
            user=get_audit_user(request, user_account),
            contract=contract or get_related_contract(instance),
        )
    except Exception:
        logger.exception('Nao foi possivel registrar o evento de auditoria.')
