from fastapi import APIRouter

from app.Basket.router import router as basket_router
from app.Categories.router import router as category_router
from app.Product.router import router as product_router
from app.user.router import router as user_router

router = APIRouter()


router.include_router(user_router)
router.include_router(product_router)
router.include_router(basket_router)
router.include_router(category_router)
