class PaymentGateway:
    pass
class ShoppingCart:
    def checkout(self, gateway):
        print("ShoppingCart USES-A PaymentGateway")
ShoppingCart().checkout(PaymentGateway())