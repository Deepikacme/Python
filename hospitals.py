class BillingService:
    def bill(self):
        print("Bill generated")
class Hospital:
    def generate_bill(self, service):
        service.bill()
Hospital().generate_bill(BillingService())