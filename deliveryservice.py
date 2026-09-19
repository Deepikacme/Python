class DeliveryService:
    def deliver(self):
        print("Food delivered")
class FoodOrder:
    def send_order(self, service):
        service.deliver()
FoodOrder().send_order(DeliveryService())