from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class StandardDelivery(Delivery):
    def calculate_charge(self):
        print("Standard delivery charge = 50")

    def deliver(self):
        print("Standard delivery in 5 days")

class ExpressDelivery(Delivery):
    def calculate_charge(self):
        print("Express delivery charge = 100")

    def deliver(self):
        print("Express delivery in 2 days")

s = StandardDelivery()
e = ExpressDelivery()

s.calculate_charge()
s.deliver()

e.calculate_charge()
e.deliver()