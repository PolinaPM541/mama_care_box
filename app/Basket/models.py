from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Basket(Base):
    __tablename__ = "basket"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    # Связи
    user: Mapped["Users"] = relationship(back_populates="baskets")
    product: Mapped["Product"] = relationship(back_populates="baskets")
