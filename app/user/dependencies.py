from datetime import datetime, timezone

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.exceptions import (
    IncorrectTokenFormaException,
    TokeAbsentException,
    TokenExpiredException,
    UserIsNotPresentHTTPException,
)
from app.user.dao import UsersDao
from app.user.models import User


def get_token(request: Request):
    token = request.cookies.get("token")
    if not token:
        raise TokeAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY_REFRESH, algorithms=settings.ALGORITHM
        )

    except JWTError:
        raise IncorrectTokenFormaException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentHTTPException
    user = await UsersDao.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentHTTPException
    return user
