class Employee:
    pass

class Doctor(Employee):
    pass

class Patient:
    pass

class BillingService:
    def bill(self):
        print("Bill generated")

class Hospital:
    def __init__(self):
        self.doctor = Doctor()
        self.patient = Patient()

    def billing(self, service):
        service.bill()

Hospital().billing(BillingService())