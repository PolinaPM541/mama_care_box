from fastapi import APIRouter

from app.Categories.dao import CategoryDao, SubcategoryDao
from app.Categories.schemas import CategoryRead, SubCategoryRead
from app.exceptions import NotFoundHTTPException, UnexpectedHTTPException

router = APIRouter(
    prefix="/category",
    tags=["category"],
)


@router.get(
    "/{category_id}",
    response_model=CategoryRead,
    responses={
        200: {"description": "Category successfully retrieved"},
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)
async def get_category(category_id) -> CategoryRead:
    """
    Get a category by id
    :param category_id:
    :return: category
    """
    try:
        category = await CategoryDao.find_by_id(category_id)
        if not category:
            raise NotFoundHTTPException
        return category
    except Exception:
        raise UnexpectedHTTPException


@router.get(
    "/subcategories/{subcategory_id}",
    response_model=SubCategoryRead,
    responses={
        200: {"description": "subcategory successfully retrieved"},
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)
async def get_subcategories(subcategory_id) -> SubCategoryRead:
    """
    Get subcategory by id
    :param: subcategory_id
    :return: subcategory
    """

    try:
        subcategory = await SubcategoryDao.find_by_id(subcategory_id)
        if not subcategory:
            raise NotFoundHTTPException
        return subcategory
    except Exception:
        raise UnexpectedHTTPException
