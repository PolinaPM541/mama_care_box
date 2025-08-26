from sqlalchemy import select

from app.Basket.models import Basket, Order, OrderItem
from app.dao.base import BaseDao
from app.database import async_session_maker


class BasketDao(BaseDao):
    model = Basket

    @classmethod
    async def get_basket_order_item(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(
                    Basket,
                    OrderItem,
                )
                .join(
                    OrderItem,
                    Basket.id == OrderItem.basket_id,
                    isouter=True,
                )
                .where(Basket.user_id == user_id)
                .order_by(OrderItem.id)
            )

            result = await session.execute(query)
            return result.mappings().all()


class OrderDao(BaseDao):
    model = Order


class OrderItemDao(BaseDao):
    model = OrderItem
