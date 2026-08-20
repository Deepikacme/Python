class Bird:
    def fly(self):
        print("Bird can fly")
class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")
class Eagle(Bird):
    def fly(self):
        print("Eagle flies very high")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
sparrow=Sparrow()
eagle=Eagle()
penguin=Penguin()
sparrow.fly()
eagle.fly()
penguin.fly()