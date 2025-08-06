from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import mapped_column
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    google_id = mapped_column(String, unique=True, index=True, nullable=True)
    email = mapped_column(String, unique=True, index=True, nullable=False)
    username = mapped_column(String, nullable=True)
    hashed_password = mapped_column(String, nullable=False)
    is_active = mapped_column(Boolean, default=True)