class Teacher:
    pass

class Student:
    pass

class NotificationService:
    def send(self):
        print("Notification sent")

class School:
    def __init__(self):
        self.teachers = [Teacher()]
        self.students = [Student()]

    def notify(self, service):
        service.send()

School().notify(NotificationService())