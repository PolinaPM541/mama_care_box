from fastapi import APIRouter, Depends

from app.Basket.dao import BasketDao, OrderDao, OrderItemDao
from app.Basket.schemas import OrderItemCreate, OrderItemRead, OrderRead
from app.exceptions import NotFoundHTTPException, UnexpectedHTTPException
from app.responses_api import responses
from app.user.auth import current_user
from app.user.models import Users

router = APIRouter(
    prefix="/basket",
    tags=["basket"],
)


@router.post(
    "/in_basket",
)
async def add_in_basket(
    basket: OrderItemCreate,
    user: Users = Depends(current_user),
):
    """
    add in basket

    :param: basket,user
    :return basket
    """
    try:
        basket_item = await OrderItemDao.create_order_item(
            user.id, basket.product_id, basket.quantity
        )
        if not basket_item:
            raise NotFoundHTTPException

        return basket_item
    except Exception:
        raise UnexpectedHTTPException


@router.get("/with_basket", response_model=list[OrderItemRead], responses=responses)
async def get_basket(user: Users = Depends(current_user)) -> list[OrderItemRead]:
    """
    get basket

    :param: user
    :return List[OrderItem]
    """
    try:
        basket = await BasketDao.get_basket_order_item(user.id)
        if not basket:
            raise NotFoundHTTPException
        return basket

    except Exception as e:
        raise UnexpectedHTTPException


@router.post("/order", response_model=OrderRead, responses=responses)
async def create_order(user: Users = Depends(current_user)) -> OrderRead:
    """
    create order

    :param: user
    :return Order
    """
    try:
        order = await OrderDao.create_order(user.id)
        if not order:
            raise NotFoundHTTPException
        return order
    except Exception:
        raise UnexpectedHTTPException
