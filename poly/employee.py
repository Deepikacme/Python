class Employee:
    def calculate_salary(self):
        print("Employee salary")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary=80000")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary=50000")
manager = Manager()
developer = Developer()
manager.calculate_salary()
developer.calculate_salary() 