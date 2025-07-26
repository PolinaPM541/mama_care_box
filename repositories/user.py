from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user import User
from schemas.user import UserCreate


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_google_id(self, google_id: str) -> User | None:
        result = await self.session.execute(select(User).filter_by(google_id=google_id))
        return result.scalars().first()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).filter_by(email=email))
        return result.scalars().first()

    async def create(self, user: UserCreate) -> User:
        db_user = User(
            google_id=user.google_id, 
            email=user.email, 
            username=user.username,
            hashed_password=user.password
            )
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user