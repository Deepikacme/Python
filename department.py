class Employee:
    def show(self):
        print("Employee")
class Department:
    def __init__(self):
        self.employees = [Employee(), Employee()]
d = Department()
for e in d.employees:
    e.show()