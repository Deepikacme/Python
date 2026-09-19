class Vehicle:
    def move(self):
        print("Vehicle moves")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
class Bus(Vehicle):
    pass
Car().move()
Bike().move()
Bus().move()