class Order:
    pass

class FoodOrder(Order):
    pass

class Restaurant:
    def __init__(self):
        self.menu = ["Pizza", "Burger"]

class PaymentService:
    def pay(self):
        print("Payment done")

class DeliveryService:
    def deliver(self):
        print("Food delivered")

class System:
    def order(self, payment, delivery):
        payment.pay()
        delivery.deliver()

System().order(PaymentService(), DeliveryService())