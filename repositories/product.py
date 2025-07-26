from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.product import Product
from schemas.product import ProductSchema


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product: ProductSchema) -> Product:
        db_product = Product(
            name=product.name, 
            description=product.description, 
            price=product.price,
            category_id=product.category_id,
            subcategory_id=product.subcategory_id
            )
        self.session.add(db_product)
        await self.session.commit()
        await self.session.refresh(db_product)
        return db_product
    
    async def get_by_id(self, product_id: int) -> Product | None:
        result = await self.session.execute(select(Product).filter_by(product_id=product_id))
        return result.scalars().first()