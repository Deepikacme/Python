from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent")

e = EmailNotification()
s = SMSNotification()

e.send()
s.send()