from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 50000

class Developer(Employee):
    def salary(self):
        return 40000

employees = [Manager(), Developer()]

for employee in employees:
    print("Salary =", employee.salary())