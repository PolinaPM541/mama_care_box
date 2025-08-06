from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.sql.annotation import Annotated

from app.user.dao import UsersDao

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/me")
async  def get_me(user:User= Annotated(UserRead,Depends(get_current_user))) -> UserRead:
    existing_user = await UsersDao.find_by_id(user.id)
    if not existing_user:
        pass
    return existing_user


@router.post("register")
async def register_user(new_user:UserCreate)->UserRead:
    existing_user = await UsersDao.find_by_if(user.id)
    if not existing_user:
        pass
    pass
