from pydantic import BaseModel, ConfigDict


class CategoryRead(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(CategoryRead):
    pass


class CategoryUpdate(CategoryRead):
    pass


class SubCategoryRead(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class SubCategoryCreate(SubCategoryRead):
    pass


class SubCategoryUpdate(SubCategoryRead):
    pass
