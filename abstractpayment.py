from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Amount: 2000")

class UPI(Payment):
    def pay(self):
        print("Payment done using UPI")

obj = UPI()
obj.pay()
obj.display_amount()