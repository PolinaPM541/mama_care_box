from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    CookieTransport,
    JWTStrategy,
)

from app.config import settings
from app.user.dependencies import get_user_manager
from app.user.models import Users

cookie_transport = CookieTransport(
    cookie_name="auth_cookie", cookie_max_age=settings.COOKIE_MAX_AGE * 7
)
bearer_transport = BearerTransport(tokenUrl="auth/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.SECRETS, lifetime_seconds=settings.JWT_LIFETIME_SECONDS
    )


cookie_backend = AuthenticationBackend(
    name="Cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


bearer_backend = AuthenticationBackend(
    name="Bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[Users, int](
    get_user_manager,
    [cookie_backend, bearer_backend],
)

current_user = fastapi_users.current_user()
