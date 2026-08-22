from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()