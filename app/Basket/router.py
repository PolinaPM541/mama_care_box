from fastapi import APIRouter, Depends

from app.Basket.dao import BasketDao
from app.Basket.schemas import BasketRead
from app.exceptions import NotFoundHTTPException, UnexpectedHTTPException
from app.user.auth import current_user
from app.user.models import Users

router = APIRouter(
    prefix="/basket",
    tags=["basket"],
)


@router.post(
    "/",
    response_model=BasketRead,
    responses={
        200: {"description": "Basket successfully created"},
        404: {"description": "Not Found"},
        500: {"description": " Internal Server Error"},
    },
)
async def add_basket(user: Users = Depends(current_user)):
    """
        add in basket
    :param: basket,user
    :return basket
    """
    try:
        basket = await BasketDao.add(
            user_id=user.id,
        )
        if not basket:
            raise NotFoundHTTPException

        return basket
    except Exception:
        raise UnexpectedHTTPException


@router.get(
    "/",
    responses={
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)
async def get_basket(user: Users = Depends(current_user)):
    """
    get basket
    :param: user
    :return basket
    """
    try:
        basket = await BasketDao.get_basket_order_item(user.id)
        if not basket:
            raise NotFoundHTTPException
        return basket

    except Exception as e:
        print(e)
