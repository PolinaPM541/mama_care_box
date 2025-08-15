import asyncio
import json
from datetime import datetime

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from app.Basket.models import Basket
from app.config import settings
from app.database import Base, async_session_maker, engine
from app.Product.Categories.models import Category, Subcategory
from app.Product.models import Order, Product
from app.user.models import User
from main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def repare_database():
    """
    create test database for test
    """

    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as f:
            return json.load(f)

    basket = open_mock_json("basket")
    users = open_mock_json("users")
    category = open_mock_json("category")
    subcategory = open_mock_json("subcategory")
    orders = open_mock_json("order")
    product = open_mock_json("product")

    for order in orders:
        order["created_at"] = datetime.strptime(order["created_at"], "%Y-%m-%dT%H:%M")

    async with async_session_maker() as session:
        for Model, values in [
            (Category, category),
            (Subcategory, subcategory),
            (Product, product),
            (User, users),
            (Basket, basket),
            (Order, orders),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop():
    """
    create new event loop
    """

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    """
    create AsyncClient for http request
    """
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as ac:
        yield ac
