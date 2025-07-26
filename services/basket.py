from models.basket import Basket
from repositories.basket import BasketRepository
from schemas.basket import BasketCreate, BasketResponse


class BasketService:
    def __init__(self, basket_repository: BasketRepository):
        self.basket_repository = basket_repository
    
    async def add_to_basket(self, basket: BasketCreate, user_id: int) -> Basket:
        return await self.basket_repository.create(basket, user_id)
    
    async def get_basket(self, user_id: int) -> list[BasketResponse] | None:
        baskets = await self.basket_repository.get_by_user_id(user_id)
        return [BasketResponse(
            id=basket.id,
            user_id=basket.user_id,
            product_id=basket.product_id,
            quantity=basket.quantity
        ) for basket in baskets] if baskets else []