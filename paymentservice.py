class PaymentService:
    def pay(self):
        print("Payment successful")
class BankAccount:
    def make_payment(self, service):
        service.pay()
BankAccount().make_payment(PaymentService())