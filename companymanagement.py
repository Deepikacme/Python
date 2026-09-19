class Employee:
    pass

class Developer(Employee):
    pass

class Department:
    pass

class PayrollService:
    def pay(self):
        print("Salary paid")

class Company:
    def __init__(self):
        self.employee = Developer()
        self.department = Department()

    def payroll(self, service):
        service.pay()

Company().payroll(PayrollService())