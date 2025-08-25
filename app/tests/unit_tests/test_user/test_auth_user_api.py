import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,is_active,is_superuser,is_verified,status_code",
    [
        ("kot@pes.com", "kot0pes", True, False, False, 201),
        ("kot@pes.com", "kot0pes", True, False, False, 400),
        ("pes@pes.com", "pesokot", True, False, False, 201),
        ("abvsda", "pesokot", True, False, False, 422),
    ],
)
async def test_register_user(
    email, password, is_active, is_superuser, is_verified, status_code, ac: AsyncClient
):
    response = await ac.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
            "is_active": is_active,
            "is_superuser": is_superuser,
            "is_verified": is_verified,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
    ],
)
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/cookie/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code
