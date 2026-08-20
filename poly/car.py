class Car:
    def start(self):
        print("Car started.")
class Bike:
    def start(self):
        print("Bike started.")
def begin(vehicle):
    vehicle.start()
car=Car()
bike=Bike()
begin(car)
begin(bike)