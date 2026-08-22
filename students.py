from abc import ABC, abstractmethod

class Student(ABC):

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    @abstractmethod
    def result(self):
        pass

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


class EngineeringStudent(Student):

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


class MedicalStudent(Student):

    def result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")


students = [
    EngineeringStudent("Deepika", 101, 85),
    MedicalStudent("Rahul", 102, 70)
]

for student in students:
    student.display()
    student.result()
    print()