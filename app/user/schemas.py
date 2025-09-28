from fastapi_users import schemas
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserRead(schemas.BaseUser[int]):

    name: str
    phone_number: PhoneNumber
    del_address: str


class UserCreate(schemas.BaseUserCreate, UserRead):
    pass


class UserUpdate(schemas.BaseUserUpdate, UserRead):
    pass
