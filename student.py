from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        print(self.name, self.age, "- Student")

class Teacher(Person):
    def role(self):
        print(self.name, self.age, "- Teacher")

class Doctor(Person):
    def role(self):
        print(self.name, self.age, "- Doctor")

s = Student("Deepika", 20)
t = Teacher("Ravi", 35)
d = Doctor("Sita", 40)

s.role()
t.role()
d.role()