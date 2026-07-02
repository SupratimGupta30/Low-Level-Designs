from abc import ABC, abstractmethod
from coin import Coin
from item import Item
from vendingmachine import VendingMachine

class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, vending_machine: VendingMachine, coin: Coin):
        pass

    @abstractmethod
    def select_product(self, vending_machine: VendingMachine, item: Item):
        pass

    @abstractmethod
    def dispense_product(self, vending_machine: VendingMachine):
        pass

    @abstractmethod
    def cancel_transaction(self, vending_machine: VendingMachine):
        pass