from datetime import date

from sqlalchemy import insert, select

from app.Basket.models import Basket, Order, OrderItem
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.exceptions import EmptyBasketHTTPException
from app.Product.dao import ProductDao


class BasketDao(BaseDao):
    model = Basket

    @classmethod
    async def get_basket_order_item(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(OrderItem)
                .join(
                    Basket,
                    OrderItem.basket_id == Basket.id,
                    isouter=True,
                )
                .where(Basket.user_id == user_id)
                .order_by(OrderItem.id)
            )

            result = await session.execute(query)
            return result.scalars().all()


class OrderDao(BaseDao):
    model = Order

    @classmethod
    async def create_order(cls, user_id: int):
        async with async_session_maker() as session:
            basket_id = await BasketDao.find_one_or_none(user_id=user_id)
            basket = await BasketDao.get_basket_order_item(user_id)

            if len(basket) == 0:
                raise EmptyBasketHTTPException

            value = sum(item.total_cost for item in basket)

            query = (
                insert(Order)
                .values(
                    user_id=user_id,
                    basket_id=basket_id.id,
                    total_cost=value,
                    created_at=date.today(),
                )
                .returning(Order)
            )

            result = await session.execute(query)
            await session.commit()
            return result.scalar()


class OrderItemDao(BaseDao):
    model = OrderItem

    @classmethod
    async def create_order_item(cls, user_id: int, product_id: int, quantity: int):
        async with async_session_maker() as session:
            product = await ProductDao.find_by_id(product_id)
            basket = await BasketDao.find_one_or_none(user_id=user_id)

            query = (
                insert(OrderItem)
                .values(
                    name=product.name,
                    price=product.price,
                    quantity=quantity,
                    product_id=product_id,
                    basket_id=basket.id,
                )
                .returning(OrderItem)
            )

            result = await session.execute(query)
            await session.commit()

            return result.scalar()
