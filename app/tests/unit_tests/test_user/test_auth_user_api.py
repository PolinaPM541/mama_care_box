import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "name,phone_number,email,password,status_code",
    [
        ("user","380997121506","kot@pes.com", "kot0pes", 201),
        ("user","380997121506","kot@pes.com", "kot0pes", 400),
        ("pset","380783225610","pes@pes.com", "pesokot", 201),
        ("swss","123456781190","abvsda", "pesokot", 422),
    ],
)
async def test_register_user(name,phone_number,email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={
            "name":name,
            "phone_number":phone_number,
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "name,phone_number,email,password,status_code",
    [
        ("user","380997121506","test@test.com", "test", 204),
    ],
)
async def test_login_user(name,phone_number,email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/cookie/login",
        data={
            "name":name,
            "phone_number":phone_number,
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code
