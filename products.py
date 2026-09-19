class Product:
    pass

class PaymentGateway:
    def pay(self):
        print("Payment done")

class ShoppingCart:
    def __init__(self):
        self.products = [Product(), Product()]

    def checkout(self, gateway):
        gateway.pay()

ShoppingCart().checkout(PaymentGateway())