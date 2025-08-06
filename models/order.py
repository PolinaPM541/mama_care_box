from sqlalchemy import DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

from models.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = mapped_column(Integer, primary_key=True, index=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    total_amount = mapped_column(Float, nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
