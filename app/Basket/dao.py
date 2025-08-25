from app.Basket.models import Order, OrderItem
from app.dao.base import BaseDao
from schemas.basket import Basket


class BasketDao(BaseDao):
    model = Basket


class OrderDao(BaseDao):
    model = Order


class OrderItemDao(BaseDao):
    model = OrderItem
