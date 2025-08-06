from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    google_id: str
    email: EmailStr
    username: str | None = None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserRead(UserBase):
    is_active: bool


class UserCreate(UserBase):
    password: str
    google_id: str | None = None


class UserInDB(UserBase):
    hashed_password: str
    is_active: bool
    google_id: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str
