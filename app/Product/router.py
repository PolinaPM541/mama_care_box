from fastapi import APIRouter

from app.exceptions import NotFoundHTTPException, UnexpectedHTTPException
from app.Product.dao import ProductDao
from app.Product.schemas import ProductRead

router = APIRouter(
    tags=["product"],
)


@router.get(
    "/{product_id}",
    response_model=ProductRead,
    responses={
        200: {"description": "Product successfully retrieved"},
        404: {"description": "Product not found"},
        500: {"description": "Internal server error"},
    },
)
async def get_product(product_id: int) -> ProductRead:
    """
    Get product by id

    :param: product_id
    :return: Product
    """
    try:
        product = await ProductDao.find_by_id(product_id)
        if not product:
            raise NotFoundHTTPException
        return product
    except Exception:
        raise UnexpectedHTTPException
