class Item:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def __eq__(self, other):
        # 1. Check if the other object is of the same type
        if not isinstance(other, Item):
            return False
        # 2. Compare the specific metadata attributes
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        # Use a tuple of the same attributes to generate a composite hash
        return hash((self.name, self.price))