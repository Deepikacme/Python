from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def study(self):
        pass

    def display(self):
        print("Course:", self.name)


class ProgrammingCourse(Course):
    def study(self):
        print("Learning Programming")


class DesignCourse(Course):
    def study(self):
        print("Learning Designing")


class BusinessCourse(Course):
    def study(self):
        print("Learning Business")


courses = [
    ProgrammingCourse("Python"),
    DesignCourse("UI Design"),
    BusinessCourse("Marketing")
]

for course in courses:
    course.display()
    course.study()
    print()