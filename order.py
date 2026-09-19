class PaymentService:
    pass
class Order:
    def pay(self, service):
        print("Order USES-A PaymentService")
Order().pay(PaymentService())