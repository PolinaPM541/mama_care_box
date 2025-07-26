from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.endpoints.user import get_session
from auth import current_user
from models.user import User
from repositories.basket import BasketRepository
from repositories.order import OrderRepository
from repositories.product import ProductRepository
from schemas.basket import BasketCreate, BasketResponse
from schemas.order import OrderCreate
from schemas.product import *
from models.product import *
from services.order import OrderService
from services.product import ProductService
from services.basket import BasketService 


router = APIRouter(tags=["basket"])

# Додавання товару в кошик
@router.post("/basket", 
             responses={
                200: {"description": "Товар створено"},
                500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
            })
async def add_to_basket(basket: BasketCreate, user: User = Depends(current_user), session: AsyncSession = Depends(get_session)):
    basket_repository = BasketRepository(session)
    basket_service = BasketService(basket_repository)
    return await basket_service.add_to_basket(basket, user.id)

# Перегляд кошика
@router.get("/basket", response_model=list[BasketResponse])
async def get_basket(user: User = Depends(current_user), session: AsyncSession = Depends(get_session)):
    basket_repository = BasketRepository(session)
    basket_service = BasketService(basket_repository)
    return await basket_service.get_basket(user.id)

# Створення замовлення з кошика
@router.post("/order", 
             responses={
                200: {"description": "Замовлення створено"},
                500: {"description": "Упс! Щось пішло не так. Спробуйте пізніше"},
            })
async def create_order(user: User = Depends(current_user), session: AsyncSession = Depends(get_session)):
    basket_repository = BasketRepository(session)
    order_repository = OrderRepository(session)
    product_repository = ProductRepository(session)
    order_service = OrderService(order_repository)

    # Отримати вміст кошика
    baskets = await basket_repository.get_by_user_id(user.id)
    if not baskets:
        raise HTTPException(status_code=400, detail="Basket is empty")
    
    # Обчислити загальну суму
    total_amount = 0
    for basket in baskets:
        product = await product_repository.get_by_id(basket.product_id)
        if product:
            total_amount += product.price * basket.quantity
    
    # Створити замовлення
    order = OrderCreate(total_amount=total_amount)
    db_order = await order_service.create_order(order, user.id)
    
    # Очистити кошик
    for basket in baskets:
        await session.delete(basket)
    await session.commit()
    
    return db_order