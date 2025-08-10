from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    google_id: Mapped[str | None] = mapped_column(unique=True)  # id with google
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __str__(self):
        return f"User email: {self.email}"
