from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary = 50000")

    def display_details(self):
        print("Manager: Team Leader")

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary = 40000")

    def display_details(self):
        print("Developer: Software Developer")

m = Manager()
d = Developer()

m.calculate_salary()
m.display_details()
d.calculate_salary()
d.display_details()