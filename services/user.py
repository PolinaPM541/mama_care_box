from models.user import User
from repositories.user import UserRepository
from schemas.user import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_or_create_user(self, google_id: str, email: str, username: str | None) -> User:
        user = await self.user_repository.get_by_google_id(google_id)
        if not user:
            user_create = UserCreate(google_id=google_id, email=email, username=username)
            user = await self.user_repository.create(user_create)
        return user