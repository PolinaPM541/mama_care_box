import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("category_id, status_code", [(1, 200)])
async def test_get_categories(category_id, status_code, ac: AsyncClient):
    response = await ac.get(f"/{category_id}")
    assert response.status_code == status_code


@pytest.mark.parametrize("subcategory_id, status_code", [(1, 200)])
async def test_get_subcategories(subcategory_id, status_code, ac: AsyncClient):
    response = await ac.get(f"/category/subcategories/{subcategory_id}")
    assert response.status_code == status_code
