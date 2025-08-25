from app.Categories.models import Category, Subcategory
from app.dao.base import BaseDao


class CategoryDao(BaseDao):
    model = Category


class SubcategoryDao(BaseDao):
    model = Subcategory
