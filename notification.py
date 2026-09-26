class NotificationService:
    def send(self):
        print("Notification sent")
class Student:
    def notify(self, service):
        service.send()
Student().notify(NotificationService())