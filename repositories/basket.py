from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.basket import Basket
from schemas.basket import BasketCreate


class BasketRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, basket: BasketCreate, user_id: int) -> Basket:
        db_basket = Basket(
            product_id=basket.product_id, user_id=user_id, quantity=basket.quantity
        )
        self.session.add(db_basket)
        await self.session.commit()
        await self.session.refresh(db_basket)
        return db_basket

    async def get_by_user_id(self, user_id: int) -> list[Basket] | None:
        result = await self.session.execute(select(Basket).filter_by(user_id=user_id))
        return result.scalars().all()
