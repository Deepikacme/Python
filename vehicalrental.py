from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

    @abstractmethod
    def vehicle_type(self):
        pass

    def display(self):
        print("Vehicle:", self.name)
        print("Rent:", self.rent)


class Car(Vehicle):
    def vehicle_type(self):
        print("Type: Car")


class Bike(Vehicle):
    def vehicle_type(self):
        print("Type: Bike")


class Bus(Vehicle):
    def vehicle_type(self):
        print("Type: Bus")


vehicles = [
    Car("Toyota", 2000),
    Bike("Honda", 800),
    Bus("Volvo", 5000)
]

for vehicle in vehicles:
    vehicle.vehicle_type()
    vehicle.display()
    print()