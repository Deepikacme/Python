class Student:
    def show(self):
        print("Student")
class College:
    def __init__(self):
        self.students = [Student(), Student()]
c = College()
for s in c.students:
    s.show()