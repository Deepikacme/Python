class Engine:
    def start(self):
        print("Engine starts")
class Car:
    def __init__(self):
        self.engine = Engine()
c = Car()
c.engine.start()