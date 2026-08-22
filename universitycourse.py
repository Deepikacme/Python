from abc import ABC, abstractmethod

class UniversityCourse(ABC):
    @abstractmethod
    def course(self):
        pass


class Engineering(UniversityCourse):
    def course(self):
        print("Engineering Course")


class Medical(UniversityCourse):
    def course(self):
        print("Medical Course")


class Management(UniversityCourse):
    def course(self):
        print("Management Course")
from abc import ABC, abstractmethod

class UniversityCourse(ABC):
    @abstractmethod
    def course(self):
        pass


class Engineering(UniversityCourse):
    def course(self):
        print("Engineering Course")


class Medical(UniversityCourse):
    def course(self):
        print("Medical Course")


class Management(UniversityCourse):
    def course(self):
        print("Management Course")


courses = [Engineering(), Medical(), Management()]

for course in courses:
    course.course()
    courses = [Engineering(), Medical(), Management()]
for course in courses:
    course.course()