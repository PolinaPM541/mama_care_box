from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.Product.models import Product


class Category(Base):
    __tablename__ = "category"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    subcategories: Mapped[list["Subcategory"]] = relationship(back_populates="category")
    products: Mapped[list["Product"]] = relationship(back_populates="category")

    def __str__(self):
        return f"category: {self.category_id}, subcategories: {self.subcategories}"


class Subcategory(Base):
    __tablename__ = "subcategory"

    subcategory_id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.category_id"))

    category: Mapped["Category"] = relationship(back_populates="subcategories")
    products: Mapped[list["Product"]] = relationship(back_populates="subcategory")

    def __str__(self):
        return f"subcategory: {self.subcategory_id}, products: {self.products}"
