from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.config import settings
from app.user.dao import UserDao
from app.user.models import Users


class UserManager(IntegerIDMixin, BaseUserManager[Users, int]):
    reset_password_token_secret = settings.SECRETS
    verification_token_secret = settings.SECRETS

    async def on_after_register(self, user: Users, request: Request | None = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: Users, token: str, request: Request | None = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: Users, token: str, request: Request | None = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(UserDao.get_user_db),
):
    yield UserManager(user_db)
