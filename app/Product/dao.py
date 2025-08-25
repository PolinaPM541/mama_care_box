from app.dao.base import BaseDao
from app.Product.models import Product


class ProductDao(BaseDao):
    model = Product
