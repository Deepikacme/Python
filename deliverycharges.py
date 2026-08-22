from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def charge(self):
        pass

class LocalDelivery(Delivery):
    def charge(self):
        return 50

class ExpressDelivery(Delivery):
    def charge(self):
        return 100

deliveries = [LocalDelivery(), ExpressDelivery()]

for delivery in deliveries:
    print("Delivery Charge =", delivery.charge())