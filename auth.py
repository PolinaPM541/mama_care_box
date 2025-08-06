from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import async_session
from models.user import User


# Налаштування бази даних
async def get_user_db(session: AsyncSession = Depends(async_session)):
    yield SQLAlchemyUserDatabase(session, User)


# Налаштування JWT
SECRET = "your_jwt_secret"
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


jwt_auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [jwt_auth_backend],
)

# Визначення current_user для використання в ендпоінтах
current_user = fastapi_users.current_user()
