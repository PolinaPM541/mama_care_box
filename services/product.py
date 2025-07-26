from models.product import Product
from repositories.product import ProductRepository
from schemas.product import ProductSchema


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def create_product(self, product: ProductSchema) -> Product:
        return await self.product_repository.create(product)
    
    async def get_product_by_id(self, product_id: int) -> Product | None:
        return await self.product_repository.get_by_id(product_id)