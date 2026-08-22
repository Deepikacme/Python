from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Amount:", self.amount)


class UPI(Payment):
    def pay(self):
        print("Payment through UPI")


class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")


class DebitCard(Payment):
    def pay(self):
        print("Payment through Debit Card")


payments = [
    UPI(1000),
    CreditCard(2000),
    DebitCard(1500)
]

for payment in payments:
    payment.pay()
    payment.display_amount()
    print()