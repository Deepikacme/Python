class Employee:
    def work(self):
        print("Employee works")
class Developer(Employee):
    pass
class Tester(Employee):
    pass
class Manager(Employee):
    pass
Developer().work()
Tester().work()
Manager().work()