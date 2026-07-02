from collections import defaultdict
from typing import DefaultDict
from item import Item

class Inventory:
    def __init__(self):
        self.stock = defaultdict(int)

    def add_item(self, item: Item, quantity: int) -> None:
        self.stock[item] += quantity

    def is_item_available(self, item: Item) -> bool:
        return self.stock[item] > 0
    
    def remove_item(self, item: Item) -> None:
        if self.is_item_available(item):
            self.stock[item] -= 1
        else:
            raise ValueError(f"Item {item.get_name()} is out of stock.")