class Department:
    pass

class Employee:
    pass

class PayrollService:
    def pay(self):
        print("Salary paid")

class Company:
    def __init__(self):
        self.departments = [Department()]
        self.employees = [Employee()]

    def payroll(self, service):
        service.pay()

Company().payroll(PayrollService())