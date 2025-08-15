from sqlalchemy import insert

from app.dao.base import BaseDao
from app.database import async_session_maker

from .models import User


class UsersDao(BaseDao):
    model = User

    @classmethod
    async def add_user(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            new_user = result.scalar()
            return new_user
