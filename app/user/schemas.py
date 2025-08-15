from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    google_id: str | None = None
    email: EmailStr
    username: str | None = None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserRead(UserBase):
    pass


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
