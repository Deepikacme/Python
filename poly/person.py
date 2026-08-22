class Person:
    def display(self):
        print("This is a Person")
class Teacher(Person):
    def display(self):
        print("This is a Teacher")
person=Person()
teacher=Teacher()
person.display()
teacher.display()