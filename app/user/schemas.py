from fastapi_users import schemas
from pydantic import Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserRead(schemas.BaseUser[int]):

    name: str = Field(min_length=2, max_length=50, pattern=r"^[a-zA-Z]+$")
    phone_number: PhoneNumber = Field(min_length=8, )
    del_address: str = Field(min_length=5)


class UserCreate(schemas.BaseUserCreate,UserRead):
    pass



class UserUpdate(schemas.BaseUserUpdate,UserRead):
    pass
