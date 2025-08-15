from datetime import date

from sqlalchemy import DECIMAL, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategory.id"))

    category: Mapped["Category"] = relationship(back_populates="products")
    subcategory: Mapped["Subcategory"] = relationship(back_populates="products")
    baskets: Mapped["Basket"] = relationship(back_populates="products")

    def __str__(self):
        return f"product: {self.id}, category: {self.category_id}, subcategory: {self.subcategory_id}"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_amount: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)
