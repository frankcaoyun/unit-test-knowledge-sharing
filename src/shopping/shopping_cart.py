from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add_item(self, item: str):
        if not isinstance(item, str):
            raise TypeError("item can only be string!")
        elif self.get_cart_size() >= self.max_size:
            raise OverflowError("cannot add more items!")
        else:
            self.items.append(item)

    def get_cart_size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            if item not in price_map:
                raise ValueError(f"price for item '{item}' not found in price_map.")
            total_price += price_map.get(item)  # can pass in anything with a .get() method
        return total_price


# Q: what if we need to pass in the `item_database` as the `price_map`?
# Q: what if it's something like an API call with the get() method`?
