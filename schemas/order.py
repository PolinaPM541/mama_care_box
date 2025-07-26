from pydantic import BaseModel
from datetime import datetime


class OrderCreate(BaseModel):
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    created_at: datetime

    class Config:
        from_attributes = True