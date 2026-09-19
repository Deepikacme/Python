class Person:
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class NotificationService:
    def send(self):
        print("Notification sent")

class School:
    def __init__(self):
        self.student = Student()
        self.teacher = Teacher()

    def notify(self, service):
        service.send()

School().notify(NotificationService())