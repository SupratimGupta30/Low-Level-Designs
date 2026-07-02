import enum


class Coin(enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def get_value(self):
        return self.value