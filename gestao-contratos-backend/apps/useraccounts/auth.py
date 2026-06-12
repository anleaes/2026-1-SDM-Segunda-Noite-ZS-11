from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from audits.services import record_audit_event
from .authentication import AUTH_COOKIE_MAX_AGE, AUTH_COOKIE_NAME, AUTH_COOKIE_SAMESITE
from .access import get_user_account, get_user_profile
from .models import UserAccount


class UserAccountAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)


def password_matches(raw_password, stored_password):
    if not stored_password:
        return False

    return check_password(raw_password, stored_password) or raw_password == stored_password


def set_auth_cookie(response, token):
    response.set_cookie(
        AUTH_COOKIE_NAME,
        token.key,
        max_age=AUTH_COOKIE_MAX_AGE,
        httponly=True,
        secure=not settings.DEBUG,
        samesite=AUTH_COOKIE_SAMESITE,
        path='/',
    )


def clear_auth_cookie(response):
    response.delete_cookie(
        AUTH_COOKIE_NAME,
        samesite=AUTH_COOKIE_SAMESITE,
        path='/',
    )


def session_data(user, account=None):
    account = account or get_user_account(user)
    return {
        'authenticated': True,
        'username': user.username,
        'profile': get_user_profile(user),
        'employee_id': account.employee_id if account else None,
    }


class UserAccountAuthToken(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = UserAccountAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        django_user = authenticate(request, username=username, password=password)
        if django_user:
            account = get_user_account(django_user)
            token, _ = Token.objects.get_or_create(user=django_user)
            response = Response({
                'detail': 'Login realizado com sucesso.',
                **session_data(django_user, account),
            })
            set_auth_cookie(response, token)
            record_audit_event(
                request=request,
                action='LOGIN',
                description=f'Usuario "{django_user.username}" entrou no sistema.',
                user_account=account,
            )
            return response

        try:
            account = UserAccount.objects.get(username=username, is_active=True)
        except UserAccount.DoesNotExist:
            return Response(
                {'non_field_errors': ['Impossivel fazer login com as credenciais fornecidas.']},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not password_matches(password, account.password):
            return Response(
                {'non_field_errors': ['Impossivel fazer login com as credenciais fornecidas.']},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user, _ = User.objects.get_or_create(
            username=account.username,
            defaults={
                'is_active': account.is_active,
                'first_name': account.employee.first_name[:150],
                'last_name': account.employee.last_name[:150],
                'email': account.employee.email,
            },
        )

        if user.is_active != account.is_active:
            user.is_active = account.is_active
            user.save(update_fields=['is_active'])

        token, _ = Token.objects.get_or_create(user=user)
        response = Response({
            'detail': 'Login realizado com sucesso.',
            **session_data(user, account),
        })
        set_auth_cookie(response, token)
        record_audit_event(
            request=request,
            action='LOGIN',
            description=f'Usuario "{account.username}" entrou no sistema.',
            user_account=account,
        )
        return response


class AuthStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(session_data(request.user))


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        record_audit_event(
            request=request,
            action='LOGOUT',
            description=f'Usuario "{request.user.username}" saiu do sistema.',
        )
        response = Response({'detail': 'Logout realizado com sucesso.'})
        clear_auth_cookie(response)
        return response
