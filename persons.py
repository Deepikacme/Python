class Person:
    def show(self):
        print("Common person details")
class Student(Person):
    pass
class Teacher(Person):
    pass
Student().show()
Teacher().show()