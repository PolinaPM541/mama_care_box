import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("product_id, status_code", [(1, 200)])
async def test_get_product(product_id, status_code, ac: AsyncClient):
    response = await ac.get(f"/{product_id}")
    assert response.status_code == status_code
