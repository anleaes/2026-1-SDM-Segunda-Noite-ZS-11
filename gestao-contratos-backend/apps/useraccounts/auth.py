from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserAccount


class UserAccountAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)


def password_matches(raw_password, stored_password):
    if not stored_password:
        return False

    return check_password(raw_password, stored_password) or raw_password == stored_password


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
            token, _ = Token.objects.get_or_create(user=django_user)
            return Response({'token': token.key})

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
        return Response({'token': token.key})
