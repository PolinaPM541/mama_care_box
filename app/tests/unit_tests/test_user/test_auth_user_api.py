import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "name,phone_number,del_address,email,password,status_code",
    [
        ("user", "+380501234567", "dniprovetrovsk", "kot@pes.com", "kot0pes", 201),
        ("user", "+380501234567", "dniprovetrovsk", "kot@pes.com", "kot0pes", 400),
        ("pset", "+380501234567", "dniprovetrovsk", "pes@pes.com", "pesokot", 201),
        ("swss", "+380501234567", "dniprovetrovsk", "abvsda", "pesokot", 422),
    ],
)
async def test_register_user(
    name, phone_number, del_address, email, password, status_code, ac: AsyncClient
):
    response = await ac.post(
        "/auth/register",
        json={
            "name": name,
            "phone_number": phone_number,
            "del_address": del_address,
            "email": email,
            "password": password,
        },
    )
    print(response.json())
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("kot@pes.com", "kot0pes", 204),
    ],
)
async def test_login_user(
     email, password, status_code, ac: AsyncClient
):
    response = await ac.post(
        "/auth/cookie/login",
        data={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code
