from pydantic import BaseModel, Field
from typing import Optional


class CategorySchema(BaseModel):
    category_id: Optional[int] = Field(default=None)
    category_name: Optional[str] = Field(default=None)
    category_description: Optional[str] = Field(default=None)

    class Config:
        from_attributes = True


class SubcategorySchema(BaseModel):
    subcategory_id: Optional[int] = Field(default=None)
    subcategory_name: Optional[str] = Field(default=None)
    subcategory_description: Optional[str] = Field(default=None)
    category_id: Optional[int] = Field(default=None)

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    product_id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    price: Optional[float] = Field(default=None)
    category_id: Optional[int] = Field(default=None)
    subcategory_id: Optional[int] = Field(default=None)

    class Config:
        from_attributes = True