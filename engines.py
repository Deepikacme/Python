class Engine:
    pass
class Car:
    def __init__(self):
        self.engine = Engine()

print("Car HAS-A Engine")