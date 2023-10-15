from unittest.mock import Mock

import pytest
from shopping.shopping_cart import ShoppingCart
from shopping.item_database import ItemDatabase


@pytest.fixture
def size():
    return 5


@pytest.fixture
def cart(size):
    return ShoppingCart(size)


@pytest.fixture
def item_1():
    return "apple"


@pytest.fixture
def item_2():
    return "orange"


@pytest.fixture
def item_3():
    return "durian"


@pytest.fixture
def items(item_1, item_2):
    return [item_1, item_2]


@pytest.fixture
def items_extra(item_1, item_2, item_3):
    return [item_1, item_2, item_3]


@pytest.fixture
def item_as_integer():
    return 123


@pytest.fixture
def item_as_list():
    return []


@pytest.fixture
def price_map(item_1, item_2):
    return {item_1: 1, item_2: 2}


@pytest.fixture
def total_price():
    return 3


# positive tests
def test_can_find_the_item_after_added_to_cart(cart, item_1):
    cart.add_item(item_1)
    assert item_1 in cart.get_items()


def test_can_get_correct_cart_size_after_added(cart, items):
    for item in items:
        cart.add_item(item)
    assert cart.get_cart_size() == 2


def test_can_get_all_items_after_added(cart, items):
    for item in items:
        cart.add_item(item)
    assert cart.get_items() == items


# negative tests
def test_cannot_add_more_items_than_max_size(cart, item_1, size):
    for _ in range(size):
        cart.add_item(item_1)

    with pytest.raises(OverflowError, match="cannot add more items!"):
        cart.add_item(item_1)


@pytest.mark.parametrize("non_string_item_fixture", ["item_as_integer", "item_as_list"])
def test_cannot_add_non_string_item(request, cart, non_string_item_fixture):
    """When you use pytest.mark.parametrize, the arguments are not treated as fixtures. Instead, they are taken as
    regular function arguments. This means you cannot directly use fixture functions within the parametrize decorator.
    You can leverage the request fixture provided by pytest. it allows you to access other fixtures dynamically.
    """
    non_string_item = request.getfixturevalue(non_string_item_fixture)
    with pytest.raises(TypeError):
        cart.add_item(non_string_item)


# positive tests
def test_can_get_correct_total_price(cart, items, price_map, total_price):
    for item in items:
        cart.add_item(item)
    assert cart.get_total_price(price_map) == total_price


# what if we need to pass in the `item_database` as the `price_map`?
# what if it's something like an API call with the get() method`?


# def test_can_get_correct_total_price(cart):
#     # arrange
#     for item in ["apple", "orange"]:
#         cart.add_item(item)

#     item_database = ItemDatabase()

#     # act & assert
#     # total price should be 3.0
#     assert cart.get_total_price(item_database) == 3.0
# but this need to wait to implement ItemDatabase.get() first. possible to bypass it?


# # use mock
# def test_can_get_correct_total_price(cart):
#     # arrange
#     for item in ["apple", "orange"]:
#         cart.add_item(item)

#     item_database = ItemDatabase()

#     def mock_get_item(item):
#         if item == "apple":
#             return 1.0
#         if item == "orange":
#             return 2.0

#     item_database.get = Mock(side_effect=mock_get_item)

#     # act & assert
#     assert cart.get_total_price(item_database) == 3.0


# # use monkeypatch
# def test_can_get_correct_total_price(monkeypatch, cart, items):
#     # arrange
#     for item in items:
#         cart.add_item(item)

#     item_database = ItemDatabase()

#     def mock_get_item(item):
#         if item == "apple":
#             return 1.0
#         if item == "orange":
#             return 2.0

#     monkeypatch.setattr(item_database, "get", mock_get_item, raising=False)

#     # act & assert
#     assert cart.get_total_price(item_database) == 3.0


# negative test
def test_cannot_get_total_price_if_item_not_in_price_map(cart, items_extra, price_map):
    for item in items_extra:
        cart.add_item(item)
    with pytest.raises(ValueError):
        cart.get_total_price(price_map)
