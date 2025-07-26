from pydantic import BaseModel


class Basket(BaseModel):
    product_id: int
    quantity: int

class BasketCreate(Basket):
    pass

class BasketResponse(Basket):
    id: int
    user_id: int

    class Config:
        from_attributes = True