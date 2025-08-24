from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategory.id"))

    subcategory: Mapped["Subcategory"] = relationship(back_populates="products")

    def __str__(self):
        return f"product: {self.id},  subcategory: {self.subcategory_id}"
