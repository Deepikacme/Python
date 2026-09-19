class Person:
    pass

class Student(Person):          # IS-A
    pass

class Course:
    pass

class Teacher(Person):          # IS-A
    pass

class Library:
    pass

class Book:
    pass

class PaymentService:
    def pay(self):
        print("Payment successful")

class NotificationService:
    def send(self):
        print("Notification sent")

class College:
    def __init__(self):
        self.student = Student()     # HAS-A
        self.course = Course()       # HAS-A
        self.library = Library()     # HAS-A

    def services(self, payment, notification):  # USES-A
        payment.pay()
        notification.send()

c = College()
c.services(PaymentService(), NotificationService())