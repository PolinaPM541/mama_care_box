import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,is_active,status_code",
    [
        ("kot@pes.com", "kotopes", True, 200),
        ("kot@pes.com", "kotOpes", True, 409),
        ("pes@pes.com", "pesokot", True, 200),
        ("abvsda", "pesokot", True, 422),
    ],
)
async def test_register_user(email, password, is_active, status_code, ac: AsyncClient):
    response = await ac.post(
        "/user/register",
        json={"email": email, "password": password, is_active: is_active},
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
        ("artem@example.com", "artem", 200),
    ],
)
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/user/login", json={"email": email, "password": password})

    assert response.status_code == status_code
