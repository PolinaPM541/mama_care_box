from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.endpoints.user import get_session
from models.product import *
from repositories.product import ProductRepository
from schemas.product import *
from services.product import ProductService

router = APIRouter(tags=["products"])


@router.get(
    "/products/{product_id}",
    responses={
        200: {"description": "Товар знайдено"},
        404: {"description": "Товар не знайдено"},
        500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
    },
)
async def get_product(product_id: int):
    try:
        if product_id <= 0:
            raise HTTPException(404, "Товар не знайдено")
        return {"product_id": product_id}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(500, "Упс! Щось пішло не так. Спробуйте пізніше")


@router.get(
    "/categories/{category_id}",
    responses={
        200: {"description": "Категорія знайдена"},
        404: {"description": "Категорія не знайдена"},
        500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
    },
)
async def get_category(category_id: int):
    try:
        if category_id <= 0:
            raise HTTPException(404, "Категорія не знайдена")
        return {"category_id": category_id}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(500, "Упс! Щось пішло не так. Спробуйте пізніше")


@router.get(
    "/subcategories/{subcategory_id}",
    responses={
        200: {"description": "Підкатегорія знайдена"},
        404: {"description": "Підкатегорія не знайдена"},
        500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
    },
)
async def get_subcategory(subcategory_id: int):
    try:
        if subcategory_id <= 0:
            raise HTTPException(404, "Підкатегорія не знайдена")
        return {"subcategory_id": subcategory_id}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(500, "Упс! Щось пішло не так. Спробуйте пізніше")


@router.get(
    "/products/{product_id}/categories/{category_id}",
    responses={
        200: {"description": "Зв’язок знайдено"},
        404: {"description": "Неприпустимі значення ID"},
        500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
    },
)
async def get_product_category(product_id: int, category_id: int):
    try:
        if product_id <= 0 or category_id <= 0:
            raise HTTPException(404, "Неприпустимі значення ID")
        return {"product_id": product_id, "category_id": category_id}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(500, "Упс! Щось пішло не так. Спробуйте пізніше")


@router.post(
    "/products",
    responses={
        200: {"description": "Товар створено"},
        500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
    },
)
async def create_product(
    product: ProductSchema, session: AsyncSession = Depends(get_session)
):
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    return await product_service.create_product(product)
