class Product:
    def show(self):
        print("Product")
class ShoppingCart:
    def __init__(self):
        self.products = [Product(), Product()]
cart = ShoppingCart()
for p in cart.products:
    p.show()