import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("kot@pes.com", "kot0pes", 201),
        ("kot@pes.com", "kot0pes", 400),
        ("pes@pes.com", "pesokot", 201),
        ("abvsda", "pesokot", 422),
    ],
)
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 204),
    ],
)
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/cookie/login",
        data={
            "username": email,
            "password": password,
        },
    )
    assert response.status_code == status_code
