from fastapi import HTTPException
from starlette import status

UserHasNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found",
)

UserHasExist = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль",
)

UserIsNotPresentHTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)
IncorrectTokenFormaException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
)
TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек",
)
TokeAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует",
)
