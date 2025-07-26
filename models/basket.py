from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column
from models.base import Base


class Basket(Base):
    __tablename__ = "basket"

    id = mapped_column(Integer, primary_key=True, index=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = mapped_column(Integer, ForeignKey("product.product.id"), nullable=False)
    quantity = mapped_column(Integer, nullable=False, default=1)
    