

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        return f'product is: {self.name} and price is: {self.price}, and quantity is: {self.quantity}'

    def total_price(self):
        return f'total price will: {self.price * self.quantity}'

beers = Product('Apple', 109, 4)