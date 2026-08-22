from abc import ABC, abstractmethod

class EmployeePayroll(ABC):
    @abstractmethod
    def salary(self):
        pass


class FullTimeEmployee(EmployeePayroll):
    def salary(self):
        print("Full Time Salary = 50000")


class PartTimeEmployee(EmployeePayroll):
    def salary(self):
        print("Part Time Salary = 25000")


class ContractEmployee(EmployeePayroll):
    def salary(self):
        print("Contract Salary = 30000")


employees = [
    FullTimeEmployee(),
    PartTimeEmployee(),
    ContractEmployee()
]

for employee in employees:
    employee.salary()