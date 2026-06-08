from rest_framework import authentication


AUTH_COOKIE_NAME = 'gestao_contratos_auth_token'
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
AUTH_COOKIE_SAMESITE = 'Lax'


class CookieTokenAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        if authentication.get_authorization_header(request):
            return super().authenticate(request)

        token = request.COOKIES.get(AUTH_COOKIE_NAME)
        if not token:
            return None

        return self.authenticate_credentials(token)
