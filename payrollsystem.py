from abc import ABC, abstractmethod

class EmployeePayroll(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass

    def display(self):
        print("Employee:", self.name)


class FullTimeEmployee(EmployeePayroll):
    def salary(self):
        print("Salary: 50000")


class PartTimeEmployee(EmployeePayroll):
    def salary(self):
        print("Salary: 25000")


class ContractEmployee(EmployeePayroll):
    def salary(self):
        print("Salary: 30000")


employees = [
    FullTimeEmployee("Deepika"),
    PartTimeEmployee("Rahul"),
    ContractEmployee("Priya")
]

for employee in employees:
    employee.display()
    employee.salary()
    print()