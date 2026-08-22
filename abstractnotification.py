from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message: Welcome to Python")

class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")

obj = EmailNotification()
obj.send()
obj.display_message()