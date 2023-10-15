from shopping.shopping_cart import ShoppingCart


def test_add_item():
    # 1. arrange
    cart = ShoppingCart(5)
    item = "apple"

    # 2. act
    cart.add_item(item)

    # 3. assert
    assert "apple" in cart.items  # Q: any concern?

    # 4. clean up (necessary when current test has side effects that may affect other tests， e.g. writing a file)

    # Q: what happens when adding an item? better to separate the test?
    # Q: better naming?


def test_can_find_the_item_after_added_to_cart():
    cart = ShoppingCart(5)
    item = "apple"
    cart.add_item(item)
    assert "apple" in cart.get_items()  # Q: how many possible reasons that the test can fail? compromise?


def test_can_get_correct_cart_size_after_added():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    # assert cart.items = items  # Q: any concern?
    # (hints: robustness, "encapsulation", bypassing)
    assert cart.get_cart_size() == 2


def test_can_get_the_correct_items_after_added():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    assert cart.get_items() == items  # Q: alternatives to check lists?


def test_can_get_correct_total_price():
    cart = ShoppingCart(5)
    items = ["apple", "orange"]
    for item in items:
        cart.add_item(item)
    price_map = {"apple": 1, "orange": 2}
    assert cart.get_total_price(price_map) == 3


# follow-up questions:
# Q: current coverage? how is it calculated?
# Q: negative tests?
# Q: repeated codes?
