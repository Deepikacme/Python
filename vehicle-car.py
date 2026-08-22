from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

c = Car()
b = Bike()

c.start()
b.start()