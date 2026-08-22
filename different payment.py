from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

payments = [CreditCard(), UPI()]

for payment in payments:
    payment.pay()