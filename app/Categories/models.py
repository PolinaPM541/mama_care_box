from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.Product.models import Product


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    subcategories: Mapped[list["Subcategory"]] = relationship(back_populates="category")

    def __str__(self):
        return f"category: {self.id}, subcategories: {self.subcategories}"


class Subcategory(Base):
    __tablename__ = "subcategory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))

    category: Mapped["Category"] = relationship(back_populates="subcategories")
    products: Mapped[list["Product"]] = relationship(back_populates="subcategory")

    def __str__(self):
        return f"subcategory: {self.id}, products: {self.products}"
