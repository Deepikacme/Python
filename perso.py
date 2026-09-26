class Person:
    pass
class Course:
    pass
class Student(Person):
    def __init__(self):
        self.course = Course()
print("Student IS-A Person")
print("Student HAS-A Course")