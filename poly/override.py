class Student:
    def display(self):
        print("Student Details")
class GraduateStudent(Student):
    def display(self):
        print("Graduate Student Details")
student=Student()
graduate=GraduateStudent()
student.display()
graduate.display()