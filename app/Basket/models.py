from datetime import date

from sqlalchemy import Computed, Date, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Basket(Base):
    __tablename__ = "basket"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["Users"] = relationship(
        "Users", back_populates="baskets", uselist=False
    )
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="basket")
    orders: Mapped["Order"] = relationship(back_populates="basket", uselist=False)


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    basket_id: Mapped[int] = mapped_column(ForeignKey("basket.id"), nullable=False)
    total_cost: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(Date, nullable=False)

    basket: Mapped["Basket"] = relationship(back_populates="orders")
    user: Mapped["Users"] = relationship(back_populates="orders")


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    basket_id: Mapped[int] = mapped_column(ForeignKey("basket.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)
    total_cost: Mapped[float] = mapped_column(Float, Computed("price*quantity"))

    basket: Mapped["Basket"] = relationship(back_populates="order_items")

    def __str__(self):
        return f"order_item: name: {self.name}, price: {self.price}, product_id: {self.product_id}"
