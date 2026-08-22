from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)

class CardPayment(Payment):
    def pay(self):
        print("Card Payment")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)

u = UPI(1000, "TXN101")
c = CardPayment(2000, "TXN102")

u.pay()
c.pay()