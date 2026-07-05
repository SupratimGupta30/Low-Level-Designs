from vendingmachinestate import VendingMachineState
from coin import Coin
from item import Item
from inventory import Inventory


class VendingMachine:
    def __init__(self):
        self.__current_state = VendingMachineState()
        self.__inventory = Inventory()
        self.__items = None
        self.balance = 0


    # Delegating methods to the current state
    def insert_coin(self, coin: Coin):
        self.__current_state.insert_coin(self, coin)

    def select_item(self, item_name):
        self.__current_state.select_product(self, item_name)
        
    def dispense_item(self, item_name):
        self.__current_state.dispense_product(self, item_name)

    def cancel_transaction(self):
        self.__current_state.cancel_transaction(self)

    #State management
    def set_state(self, state: VendingMachineState):
        self.__current_state = state

    # Balance management
    def add_balance(self, amount: int):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def reset_balance(self):
        self.balance = 0

    # Inventory management
    def get_inventory(self) -> Inventory:
        return self.__inventory

    # Item helpers

    def set_selected_item(self, item: Item):
        self.__items = item

    def get_selected_item(self):
        return self.__items

    