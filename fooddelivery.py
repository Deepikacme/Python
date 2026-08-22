from abc import ABC, abstractmethod

class Delivery(ABC):
    def __init__(self, order):
        self.order = order

    @abstractmethod
    def deliver(self):
        pass

    def display(self):
        print("Order:", self.order)


class BikeDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Bike")


class CarDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Car")


class DroneDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Drone")


deliveries = [
    BikeDelivery("Pizza"),
    CarDelivery("Burger"),
    DroneDelivery("Cake")
]

for delivery in deliveries:
    delivery.display()
    delivery.deliver()
    print()