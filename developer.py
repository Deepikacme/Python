class Employee:
    pass
class Laptop:
    pass
class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()
print("Developer IS-A Employee")
print("Developer HAS-A Laptop")