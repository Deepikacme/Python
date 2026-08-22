from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

    def refund(self):
        print("UPI refund processed")

class CreditCard(Payment):
    def pay(self):
        print("Payment through Credit Card")

    def refund(self):
        print("Credit Card refund processed")

class NetBanking(Payment):
    def pay(self):
        print("Payment through Net Banking")

    def refund(self):
        print("Net Banking refund processed")

u = UPI()
c = CreditCard()
n = NetBanking()

u.pay()
u.refund()

c.pay()
c.refund()

n.pay()
n.refund()