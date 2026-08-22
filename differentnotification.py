from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:
    notification.send()