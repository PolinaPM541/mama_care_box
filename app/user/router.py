from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated

from app.user.dao import UsersDao
from app.user.schemas import UserCreate, UserRead
from models.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/me")
async def get_me(
    user: User = Annotated[UserRead, Depends(get_current_user)]
) -> UserRead:
    """
    get user info

    param:
        user
    return:
        existing_user

    """

    existing_user = await UsersDao.find_by_id(user.id)
    if not existing_user:
        pass
    return existing_user


@router.post("register")
async def register_user(new_user: UserCreate) -> str:
    """
    register new user
    param:
        new_user
    return
        access_token
    """

    existing_user = await UsersDao.find_by_id(new_user.id)
    if not existing_user:
        pass
