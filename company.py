class Department:
    def show(self):
        print("Department")
class Company:
    def __init__(self):
        self.departments = [Department(), Department()]
c = Company()
for d in c.departments:
    d.show()