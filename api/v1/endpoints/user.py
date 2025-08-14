# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from auth import fastapi_users
# from models.base import async_session
# from models.user import User
# from repositories.user import UserRepository
# from schemas.user import UserCreate, UserResponse
# from services.user import UserService
#
# router = APIRouter(tags=["users"])
#
#
# async def get_session():
#     async with async_session() as session:
#         yield session
#
#
# # Отримання поточного користувача
# current_user = fastapi_users.current_user()
#
#
# @router.get("/me", response_model=UserResponse)
# async def get_me(user: User = Depends(current_user)):
#     return user
#
#
# # Створення користувача (для тестування)
# @router.post("/users", response_model=UserResponse)
# async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
#     user_repository = UserRepository(session)
#     user_service = UserService(user_repository)
#     return await user_service.get_or_create_user(
#         google_id=user.google_id, email=user.email, username=user.username
#     )
