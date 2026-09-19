class Employee:
    pass
class Company:
    def __init__(self):
        self.employees = [Employee(), Employee()]

print("Company HAS-A Employees")