class Keyboard:
    pass
class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()
print("Laptop HAS-A Keyboard")