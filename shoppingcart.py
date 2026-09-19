class PaymentGateway:
    def pay(self):
        print("Payment completed")
class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay()
ShoppingCart().checkout(PaymentGateway())