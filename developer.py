from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print(self.name, "- Manager - Salary:", self.salary)

class Developer(Employee):
    def work(self):
        print(self.name, "- Developer - Salary:", self.salary)

class Tester(Employee):
    def work(self):
        print(self.name, "- Tester - Salary:", self.salary)

m = Manager("Ravi", 50000)
d = Developer("Deepika", 40000)
t = Tester("Sita", 35000)

m.work()
d.work()
t.work()