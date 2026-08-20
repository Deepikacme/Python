class Dog:
    def bark(self):
        print("Dog says:BowBow!")
class RobotDog:
    def bark(self):
        print("Robo Dog says: BeepBow!")
def make_bark(obj):
    obj.bark()
d=Dog()
r=RobotDog()
make_bark(d)
make_bark(r)