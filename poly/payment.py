class Payment:
    def pay(self):
        print("Payment Process")
class CreditCardPayment(Payment):
    def pay(self):
        print("Payment made using Credit Card")
class UPIPayment(Payment):
    def pay(self):
        print("Payment made using UPI")
class CashPayment(Payment):
    def pay(self):
        print("Payment made using Cash")
credit=CreditCardPayment()
upi=UPIPayment()
cash=CashPayment()
credit.pay()
upi.pay()
cash.pay()