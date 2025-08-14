import asyncio
import json

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker, engine
from main import app as fastapi_app
from models.user import User


@pytest.fixture(scope="session", autouse=True)
async def repare_database():
    """
    create test database for testing
    """

    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as f:
            return json.load(f)

    users = open_mock_json("users")

    async with async_session_maker() as session:
        for Model, values in [
            (User, users),
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
