from pydantic import BaseModel


class BasketRead(BaseModel):
    product_id: int
    quantity: int


class BasketCreate(BasketRead):
    pass


class BasketResponse(BasketRead):
    id: int
    user_id: int

    class Config:
        from_attributes = True
