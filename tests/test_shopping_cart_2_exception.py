import pytest

from shopping.shopping_cart import ShoppingCart


# positive tests
def test_can_find_the_item_after_added_to_cart():
    cart = ShoppingCart(5)
    item = "apple"
    cart.add_item(item)
    assert "apple" in cart.get_items()


def test_can_get_correct_cart_size_after_added():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    assert cart.get_cart_size() == 2


def test_can_get_all_items_after_added():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    assert cart.get_items() == items


# negative tests
def test_cannot_add_more_items_than_max_size():
    cart = ShoppingCart(5)
    item = "apple"
    for _ in range(5):
        cart.add_item(item)

    with pytest.raises(OverflowError, match="cannot add more items!"):
        cart.add_item(item)


def test_cannot_add_integer_item():
    cart = ShoppingCart(5)
    item = 123
    with pytest.raises(TypeError):
        cart.add_item(item)


def test_cannot_add_list_item():
    cart = ShoppingCart(5)
    item = []
    with pytest.raises(TypeError):
        cart.add_item(item)  # Q: essentially the same test as above. simplify?


# positive tests
def test_can_get_correct_total_price():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    price_map = {"apple": 1, "orange": 2}
    assert cart.get_total_price(price_map) == 3


# negative test
def test_cannot_get_total_price_if_item_not_in_price_map():
    cart = ShoppingCart(5)
    items = ["apple", "orange", "durian"]
    for item in items:
        cart.add_item(item)
    price_map = {"apple": 1, "orange": 2}
    # with pytest.raises(TypeError):
    #     cart.get_total_price(price_map)  # does it work?
    # (hint: make sure it can fail without implementing the actual code)
    with pytest.raises(ValueError):
        cart.get_total_price(price_map)


# Q: repeated codes?
