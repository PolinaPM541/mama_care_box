import pytest

from app.Basket.dao import BasketDao, OrderDao, OrderItemDao


@pytest.mark.parametrize(
    "user_id,name,price,quantity,total_cost",
    [
        (1, "1954", 100, 1, 100),
    ],
)
async def test_create_item_in_basket(user_id, name, price, quantity, total_cost):
    response = await BasketDao.get_basket_order_item(user_id)

    if response == []:
        assert 200, []

    item = response[0]
    assert item.name == name
    assert item.price == price
    assert item.quantity == quantity
    assert item.total_cost == total_cost


@pytest.mark.parametrize(
    "user_id,basket_id,total_cost",
    [
        (
            1,
            1,
            100,
        ),
    ],
)
async def test_create_order(user_id, basket_id, total_cost):
    response = await OrderDao.create_order(user_id)
    if response == []:
        assert 200, []

    assert response.basket_id == basket_id
    assert response.total_cost == total_cost
    assert response.user_id == user_id


@pytest.mark.parametrize(
    "user_id,product_id,quantity,name,price,total_cost",
    [
        (1, 1, 1, "1954", 100, 100),
    ],
)
async def test_create_order_item(
    user_id, product_id, quantity, name, price, total_cost
):
    response = await OrderItemDao.create_order_item(user_id, product_id, quantity)
    if response == []:
        assert 200, []

    assert response.name == name
    assert response.price == price
    assert response.quantity == quantity
    assert response.total_cost == total_cost
