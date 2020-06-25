from datetime import timedelta

from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


def has_expired(token, lifespan=7):
    return timezone.now() > (token.created + timedelta(lifespan))


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
        if has_expired(token):
            raise exceptions.AuthenticationFailed('Token has expired')
        return (token.user, token)
