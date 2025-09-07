import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "product_id,quantity,status_code",
    [
        (1, 1, 200),
        (1, 2, 200),
        (1, 3, 200),
    ],
)
async def test_add_in_basket(
    product_id, quantity, status_code, authenticated_ac: AsyncClient
):
    response = await authenticated_ac.post(
        "/basket/in_basket",
        json={
            "product_id": product_id,
            "quantity": quantity,
        },
    )

    response.status_code = status_code
    response.quantity_id = quantity
    response.product_id = product_id


@pytest.mark.parametrize(
    "status_code",
    [
        (200,),
    ],
)
async def test_get_basket(status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.get(
        "/basket/with_basket",
    )
    response.status_code = status_code


@pytest.mark.parametrize(
    "status_code",
    [
        (200),
    ],
)
async def test_create_order(status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post(
        "/basket/order",
    )
    response.status_code = status_code
