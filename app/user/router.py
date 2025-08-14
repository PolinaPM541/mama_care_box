from typing import Annotated, Any

from fastapi import APIRouter, Depends, Response

from app.exceptions import (
    IncorrectEmailOrPasswordException,
    UserHasExist,
    UserHasNotExist,
)
from app.user.auth import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_password_hash,
)
from app.user.dao import UsersDao
from app.user.dependencies import get_current_user
from app.user.models import User
from app.user.schemas import UserCreate, UserLogin, UserRead

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


#
@router.get("/me", response_model=UserRead)
async def get_me(user: User = Annotated[UserRead, Depends(get_current_user)]) -> Any:
    """
    get user info

    param:
        user
    return:
        existing_user
    """

    existing_user = await UsersDao.find_by_id(user.id)
    if not existing_user:
        raise UserHasNotExist
    return existing_user


@router.post("register", response_model=UserRead)
async def register_user(new_user: UserCreate) -> Any:
    """
    register new user

    param:
        new_user
    return
        user
    """

    existing_user = await UsersDao.find_by_id(new_user.id)
    if existing_user:
        raise UserHasExist
    new_user.password = get_password_hash(new_user.password)
    user = await UsersDao.add(**new_user.model_dump())
    print(user)
    return user


@router.post("/login", response_model=UserRead)
async def login_user(response: Response, user_data: UserLogin) -> Any:
    """
    login user

    param:
        user_data
    return:
        access_token
    """
    user = await authenticate_user(user_data.emal, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    refresh_token = create_refresh_token({"sub": user.id})
    response.set_cookie(
        "token", value=refresh_token, httponly=True, secure=True, samesite="strict"
    )

    access_token = create_access_token({"sub": user.id})
    return access_token
