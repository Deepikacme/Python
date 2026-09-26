class Product:
    pass

class Mobile(Product):
    pass

class PaymentService:
    def pay(self):
        print("Payment successful")

class DeliveryService:
    def deliver(self):
        print("Product delivered")

class Cart:
    def __init__(self):
        self.product = Mobile()

    def checkout(self, payment, delivery):
        payment.pay()
        delivery.deliver()

Cart().checkout(PaymentService(), DeliveryService())