from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDao
from app.database import get_async_session
from app.user.models import OAuthnAccount, Users


class UserDao(BaseDao):
    model = Users

    @classmethod
    async def get_user_db(cls, session: AsyncSession = Depends(get_async_session)):
        yield SQLAlchemyUserDatabase(session, Users, OAuthnAccount)

