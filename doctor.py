class Doctor:
    pass

class Patient:
    pass

class BillingService:
    def bill(self):
        print("Hospital bill generated")

class Hospital:
    def __init__(self):
        self.doctors = [Doctor()]
        self.patients = [Patient()]

    def billing(self, service):
        service.bill()

Hospital().billing(BillingService())