class Account:
    pass

class SavingsAccount(Account):
    pass

class Customer:
    pass

class PaymentService:
    def pay(self):
        print("Payment successful")

class Bank:
    def __init__(self):
        self.customer = Customer()
        self.account = SavingsAccount()

    def payment(self, service):
        service.pay()

Bank().payment(PaymentService())