class Vehicle:
    def move(self):
        print("Vehicle moves")
class Car(Vehicle):
    pass
c=Car()
c.move()