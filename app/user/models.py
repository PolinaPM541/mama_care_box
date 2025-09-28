from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseOAuthAccountTable,
    SQLAlchemyBaseUserTable,
)
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from app.Basket.models import Basket, Order
from app.database import Base


class OAuthnAccount(SQLAlchemyBaseOAuthAccountTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
        )


class Users(SQLAlchemyBaseUserTable[int], Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    oauth_accounts: Mapped[list[OAuthnAccount]] = relationship(
        "OAuthnAccount", lazy="joined"
    )

    orders: Mapped["Order"] = relationship("Order", back_populates="user")
    baskets: Mapped["Basket"] = relationship("Basket", back_populates="user")
