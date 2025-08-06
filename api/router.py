from fastapi import APIRouter

from api.v1.endpoints.basket import router as basket_router
from api.v1.endpoints.product import router as product_router
from api.v1.endpoints.user import router as user_router

router = APIRouter()


router.include_router(user_router)
router.include_router(product_router)
router.include_router(basket_router)
