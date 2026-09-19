class Product:
    pass

class PaymentService:
    def pay(self):
        print("Payment successful")

class DeliveryService:
    def deliver(self):
        print("Order delivered")

class OnlineOrder:
    def __init__(self):
        self.products = [Product()]

    def checkout(self, payment, delivery):
        payment.pay()
        delivery.deliver()

o = OnlineOrder()
o.checkout(PaymentService(), DeliveryService())