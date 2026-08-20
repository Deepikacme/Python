class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts")
class Bike(Vehicle):
    def start(self):
        print("Bike starts")
class Bus(Vehicle):
    def start(self):
        print("Bus starts")
c=Car()
b=Bike()
bs=Bus()
c.start()
b.start()
bs.start()