from models.order import Order
from repositories.order import OrderRepository
from schemas.order import OrderCreate

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    async def create_order(self, order: OrderCreate, user_id: int) -> Order:
        return await self.order_repository.create(order, user_id)