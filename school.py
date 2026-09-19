class Teacher:
    def show(self):
        print("Teacher")
class Student:
    def show(self):
        print("Student")
class School:
    def __init__(self):
        self.teacher = Teacher()
        self.student = Student()
s = School()
s.teacher.show()
s.student.show()