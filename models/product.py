from datetime import datetime
import uuid
from sqlalchemy import Boolean, DECIMAL, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

from models.base import Base


class Category(Base):
    __tablename__ = "category"

    category_id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)

    subcategories = relationship("Subcategory",back_populates="category")
    product = relationship("Product",back_populates="category")

    async def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description,
        }

class Subcategory(Base):
    __tablename__ = "subcategory"

    subcategory_id = mapped_column(Integer, primary_key=True, unique=True)
    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    category_id = mapped_column(Integer, ForeignKey("category.category_id"))

    category = relationship("Category",back_populates="subcategories")
    product = relationship("Product",back_populates="subcategory")

    async def to_dict(self):
        return {
            "subcategory_id": self.subcategory_id,
            "name": self.name,
            "description": self.description,
            "category_id": self.category_id,
        }
    
class Product(Base):
    __tablename__ = "product"

    product_id = mapped_column(Integer, primary_key=True, unique=True)
    name = mapped_column(String, nullable=False)
    description = mapped_column(String, nullable=False)
    price = mapped_column(DECIMAL, nullable=False)
    category_id = mapped_column(Integer, ForeignKey("category.category_id"))
    subcategory_id = mapped_column(Integer, ForeignKey("subcategory.subcategory_id"))

    category = relationship("Category",back_populates="product")
    subcategory = relationship("Subcategory",back_populates="product")

    async def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "subcategory_id": self.subcategory_id,
        }