from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(self.brand, self.model, "started")

    def stop(self):
        print(self.brand, self.model, "stopped")

c = Car("Toyota", "Innova")

c.start()
c.stop()