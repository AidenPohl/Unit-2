import random

"""
Name: Aiden Pohl
Date: 3/6/2025
Description: Self Kiosk Project
"""

class Register:

    def __init__(self, transaction_total: int, total_items :int, discount_total: int, transaction_id: int ) -> None:

        self.transaction_total = transaction_total
        self.total_items = total_items
        self.discount_total = discount_total
        self.transaction_id = transaction_id


    def addItem(self) -> None:
        ItemInput = input("Please input a item: ")
        PriceInput = float(input("Please input the price of the item: "))

        self.transaction_total += PriceInput

        self.total_items += 1
        print(f"The transaction total is now {self.transaction_total:.2f}")
        print(f"You have {self.total_items} items in your cart")

    def makeID(self) -> None:
        pass
            
























def main():
    register = Register(0,0,0,0)
    register.addItem()
    register.addItem()

if __name__ == '__main__':
    main()