from rest_framework.permissions import BasePermission

from .models import UserAccount


ADMIN = 'ADMIN'
MANAGER = 'GERENTE'
EMPLOYEE = 'FUNCIONARIO'
LEGACY_EMPLOYEE = 'OPERADOR'


def get_user_account(user):
    if not user or not getattr(user, 'is_authenticated', False):
        return None

    return UserAccount.objects.select_related('employee').filter(
        username=user.username,
        is_active=True,
    ).first()


def get_user_profile(user):
    account = get_user_account(user)
    if account:
        if account.profile == LEGACY_EMPLOYEE:
            return EMPLOYEE

        return account.profile

    if getattr(user, 'is_superuser', False):
        return ADMIN

    return None


class RoleBasedPermission(BasePermission):
    def has_permission(self, request, view):
        profile = get_user_profile(request.user)
        action = getattr(view, 'action', None)

        if profile == ADMIN:
            return True

        if profile == MANAGER:
            allowed_actions = getattr(view, 'manager_allowed_actions', None)
            return allowed_actions is None or action in allowed_actions

        if profile == EMPLOYEE:
            allowed_actions = getattr(view, 'employee_allowed_actions', ())
            return action in allowed_actions

        return False


class RoleScopedViewSetMixin:
    permission_classes = [RoleBasedPermission]
    manager_allowed_actions = None
    employee_allowed_actions = ()
    employee_filter = None

    def get_queryset(self):
        queryset = super().get_queryset()

        if get_user_profile(self.request.user) != EMPLOYEE:
            return queryset

        account = get_user_account(self.request.user)
        if not account or not self.employee_filter:
            return queryset.none()

        scoped_ids = queryset.filter(**{
            self.employee_filter: account.employee_id,
        }).values('pk')

        return queryset.filter(pk__in=scoped_ids)
