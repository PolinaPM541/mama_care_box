from fastapi import HTTPException
from starlette import status

UserIsNotPresentHTTPException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
)


NotFoundHTTPException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=" Not Fount"
)

UnexpectedHTTPException = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
)

EmptyBasketHTTPException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Empty Basket was found",
)
