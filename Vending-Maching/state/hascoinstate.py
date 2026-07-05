from vendingmachinestate import VendingMachineState


class HasCoinState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted. Please select a product.")

    def select_product(self, product_code):
        if self.vending_machine.is_product_available(product_code):
            self.vending_machine.dispense_product(product_code)
            self.vending_machine.set_state(self.vending_machine.no_coin_state)
        else:
            print("Selected product is out of stock. Please select another product.")

    def dispense_product(self):
        print("Please select a product first.")