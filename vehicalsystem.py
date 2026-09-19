class Vehicle:
    pass

class Car(Vehicle):
    pass

class Customer:
    pass

class PaymentService:
    def pay(self):
        print("Rental payment done")

class Rental:
    def __init__(self):
        self.vehicle = Car()
        self.customer = Customer()

    def payment(self, service):
        service.pay()

Rental().payment(PaymentService())