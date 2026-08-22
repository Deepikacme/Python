from abc import ABC, abstractmethod

class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass

class OnlineCourse(Course):
    def start(self):
        print("Online Course:", self.course_name)
        print("Duration:", self.duration)

class OfflineCourse(Course):
    def start(self):
        print("Offline Course:", self.course_name)
        print("Duration:", self.duration)

o = OnlineCourse("Python", "3 Months")
f = OfflineCourse("Java", "6 Months")

o.start()
f.start()