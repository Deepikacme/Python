class Vehicle:
    pass
class Engine:
    pass
class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()
print("Car IS-A Vehicle")
print("Car HAS-A Engine")