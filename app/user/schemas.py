from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr, model_validator, ValidationError, Field

from app.user.auth import fastapi_users


class UserRead(schemas.BaseUser[int]):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = Field(None, min_length=8)

    @model_validator(mode='after')
    def check_contact_info(self):
        if not self.phone_number and not self.email:
            raise ValidationError('Please provide phone number or email')

        return self


class UserCreate(schemas.BaseUserCreate):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = Field(None, min_length=8)

    @model_validator(mode='after')
    def check_contact_info(self):
        if not self.phone_number and not self.email:
            raise ValidationError('Please provide phone number or email')

        return self


class UserUpdate(schemas.BaseUserUpdate, UserCreate):
    pass
