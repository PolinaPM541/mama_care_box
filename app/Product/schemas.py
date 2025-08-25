from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    name: str
    description: str
    price: int

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(ProductRead):
    subcategory_id: int


class ProductUpdate(ProductRead):
    subcategory_id: int
