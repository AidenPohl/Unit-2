#Imports Random to use to make a random transaction id
import random

"""
Name: Aiden Pohl
Date: 3/6/2025
Description: Self Kiosk Project
"""


class Register:

    def __init__(self,resets: int, items: dict,transaction_total: int, total_items :int, discount_total: int, transaction_id: int, rewards_member: False ) -> None:

        '''
        Args:
            transaction
        
        '''
        self.resets = 0
        self.items = {}
        self.transaction_total = 0
        self.total_items = 0
        self.discount_total = 0
        if self.resets == 0:
            self.transaction_id = random.randint(1000000000,9999999999)
        else:
            pass
        self.rewards_member = False




    def getTotal(self) -> None:
        return self.transaction_total

    def addItem(self) -> None:

        while True:
            ItemInput = input("Please input a item: ")
            PriceInput = float(input("Please input the price of the item: "))

            self.items[ItemInput] = PriceInput
            self.transaction_total += PriceInput

            self.total_items += 1
            print(f"You've added '{ItemInput.upper()}' to your cart")
            print(f"The transaction total is now {self.transaction_total:.2f}")
            print(f"You have {self.total_items} items in your cart")
            Another = input("Would you like to add another item?(y/n): ")
            if Another.lower() == 'y':
                True
            if Another.lower() == 'n':
                break
            else:
                Another = input("Sorry, input not recognized, please try again: ")

    def applyDiscount(self) -> None:
        Discount = 0.1
        DiscountAmount = self.transaction_total * Discount
        self.discount_total = DiscountAmount
        self.transaction_total -= DiscountAmount
        print(f"Discount recieved, ${DiscountAmount:.2f} was taken off your order")
    def finalizeTransaction(self) -> None:
        print("-Finalizing Transaction-")
        print(f"Pre Total: ${self.transaction_total:.2f}")
        
        self.rewards_member = input("Are you a rewards member?(y/n): ")
        if self.rewards_member == 'y':
            self.applyDiscount()
            print(f"Total after discount: ${self.transaction_total:.2f}")
        else:
            pass


    def takePayment(self) -> None:
        PaymentMethod = input("Please select payment method (cash only): ").lower()

        while PaymentMethod != 'cash':
            PaymentMethod = input(f"Sorry, {PaymentMethod} is not accepted, please use another payment method: ")
        else:
            cash = float(input("Please input the amount of cash put in: "))
            while cash < self.transaction_total:
                cash = "CashTaken"
                cash = float(input("Not enough cash recieved.\n*Dispensing Cash*...\n Please input more cash: "))
            else:
                self.giveChange(cash)
    
    def giveChange(self, cash: float) -> None:
        if cash > self.transaction_total:
            change = cash - self.transaction_total
            print(f"Change due: ${change:.2f}")
        else:
            print("No change due")


    def print_receipt(self) -> None:
        print("--- Receipt ---")
        print(f"Transaction ID: {self.transaction_id}")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")
        print(f"Total Items: {self.total_items}")
        print(f"Pre-Total: ${self.transaction_total + self.discount_total:.2f}")
        print(f"Discount Applied to Pre-Total - ${self.discount_total:.2f}")
        print(f"Final Total: ${self.transaction_total:.2f}")
        print("Thanks for shopping here!")
        kiosk_reset = input("Are you done shopping?(y/n): ").lower
        if kiosk_reset == 'n':
            self.reset_transaction()
        else:
            pass
    def reset_transaction(self) -> None:
        self.transaction_total = 0
        self.total_items = 0
        self.discount_total = 0
        self.rewards_member = False



def main():
    print("Welcome to Self-Checkout!")
    register = Register(0,0,0,0,0,0,False)
    register.addItem()
    register.finalizeTransaction()
    register.takePayment()
    register.print_receipt()
if __name__ == '__main__':
    main()