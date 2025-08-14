from sqlalchemy import DECIMAL, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL, nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.category_id"))
    subcategory_id: Mapped[int] = mapped_column(
        ForeignKey("subcategory.subcategory_id")
    )

    category: Mapped["Category"] = relationship(back_populates="products")
    subcategory: Mapped["Subcategory"] = relationship(back_populates="products")

    def __str__(self):
        return f"product: {self.product_id}, category: {self.category_id}, subcategory: {self.subcategory_id}"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped["datetime"] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
