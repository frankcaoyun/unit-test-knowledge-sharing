import pytest

from shopping.shopping_cart import ShoppingCart


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


# def test_cannot_add_integer_item(cart, item_as_integer):
#     with pytest.raises(TypeError):
#         cart.add_item(item_as_integer)

# def test_cannot_add_list_item(cart, item_as_list):
#     with pytest.raises(TypeError):
#         cart.add_item(item_as_list)  # Q: essentially the same test as above. simplify?


@pytest.mark.parametrize("non_string_item", [123, []])  # Q: How to parametrize fixtures?
def test_cannot_add_non_string_item(non_string_item):
    cart = ShoppingCart(5)
    with pytest.raises(TypeError):
        cart.add_item(non_string_item)


# @pytest.mark.parametrize("non_string_item", [item_as_integer, item_as_list])
# def test_cannot_add_non_string_item(cart, non_string_item):
#     with pytest.raises(TypeError):
#         cart.add_item(non_string_item)  # working? (hint: passing an instance vs passing the fixture function)


# @pytest.mark.parametrize("non_string_item_fixture", ["item_as_integer", "item_as_list"])
# def test_cannot_add_non_string_item(request, cart, non_string_item_fixture):
#     """When you use pytest.mark.parametrize, the arguments are not treated as fixtures. Instead, they are taken as
#     regular function arguments. This means you cannot directly use fixture functions within the parametrize decorator.
#     You can leverage the request fixture provided by pytest. it allows you to access other fixtures dynamically.
#     """
#     non_string_item = request.getfixturevalue(non_string_item_fixture)
#     with pytest.raises(TypeError):
#         cart.add_item(non_string_item)


# positive tests
def test_can_get_correct_total_price(cart, items, price_map, total_price):
    for item in items:
        cart.add_item(item)
    assert cart.get_total_price(price_map) == total_price


# negative test
def test_cannot_get_total_price_if_item_not_in_price_map(cart, items_extra, price_map):
    for item in items_extra:
        cart.add_item(item)
    with pytest.raises(ValueError):
        cart.get_total_price(price_map)
