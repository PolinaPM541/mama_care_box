from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.Basket.models import Basket, Order
from app.database import Base


class Users(SQLAlchemyBaseUserTable[int], Base):

    id: Mapped[int] = mapped_column(primary_key=True)

    orders: Mapped["Order"] = relationship("Order", back_populates="user")
    baskets: Mapped["Basket"] = relationship("Basket", back_populates="user")
