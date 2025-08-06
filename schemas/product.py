from typing import Optional

from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    category_id: int | None = Field(default=None)
    category_name: str | None = Field(default=None)
    category_description: str | None = Field(default=None)

    class Config:
        from_attributes = True


class SubcategorySchema(BaseModel):
    subcategory_id: int | None = Field(default=None)
    subcategory_name: str | None = Field(default=None)
    subcategory_description: str | None = Field(default=None)
    category_id: int | None = Field(default=None)

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    product_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    price: float | None = Field(default=None)
    category_id: int | None = Field(default=None)
    subcategory_id: int | None = Field(default=None)

    class Config:
        from_attributes = True
