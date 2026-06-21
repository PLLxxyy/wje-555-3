from datetime import datetime, timedelta, timezone

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions


def create_token(user):
    payload = {
        "sub": str(user.id),
        "username": user.username,
        "role": user.role,
        "exp": datetime.now(timezone.utc) + timedelta(hours=settings.JWT_EXPIRE_HOURS),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")


class JWTAuthentication(authentication.BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        header = authentication.get_authorization_header(request).decode("utf-8")
        if not header:
            return None
        parts = header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            raise exceptions.AuthenticationFailed("Invalid authorization header")
        try:
            payload = jwt.decode(parts[1], settings.JWT_SECRET, algorithms=["HS256"])
        except jwt.PyJWTError as exc:
            raise exceptions.AuthenticationFailed("Invalid token") from exc
        User = get_user_model()
        try:
            return (User.objects.get(id=payload["sub"]), None)
        except User.DoesNotExist as exc:
            raise exceptions.AuthenticationFailed("User not found") from exc

