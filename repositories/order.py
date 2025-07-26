from sqlalchemy.ext.asyncio import AsyncSession
from models.order import Order
from schemas.order import OrderCreate

class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, order: OrderCreate, user_id: int) -> Order:
        db_order = Order(total_amount=order.total_amount, user_id=user_id)
        self.session.add(db_order)
        await self.session.commit()
        await self.session.refresh(db_order)
        return db_order