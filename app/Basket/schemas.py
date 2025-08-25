from datetime import date

from pydantic import BaseModel, ConfigDict


class BasketRead(BaseModel):
    pass

    model_config = ConfigDict(from_attributes=True)


class BasketCreate(BaseModel):
    user_id: int


class BasketUpdate(BaseModel):
    pass


class OrderRead(BaseModel):
    created_at: date

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    user_id: int
    basket_id: int
    total_cost: float
    created_at: date


class OrderUpdate(OrderCreate):
    pass


class OrderItemRead(BaseModel):
    name: str
    price: float
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(BaseModel):
    name: str
    price: float
    product_id: int
    basket_id: int
    quantity: int
    total_cost: float


class OrderItemUpdate(OrderItemCreate):
    pass
