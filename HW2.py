class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def total_cost(self, quant: int) -> float:
        return round(self.price * quant, 2)

    def __repr__(self) -> str:
        return f'{self.name} cost {self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __float__(self) -> float:
        return self.price

    def __str__(self) -> str:
        return self.name


class ShoppingCart:
    def __init__(self) -> None:
        self.goods = []
        self.quant = []

    def add_goods(self, prod: Product, quant: int):
        if prod in self.goods:
            self.quant[self.goods.index(prod)] += quant
            return
        self.goods.append(prod)
        self.quant.append(quant)

    def get_total(self) -> float:
        temp = 0
        for prod, quant in self:
            temp += prod.total_cost(quant)
        return round(temp, 2)

    def __repr__(self) -> str:
        return f'{list(zip(self.goods, self.quant))} '

    def __float__(self):
        return self.get_total()

    def __iter__(self) -> iter:
        return zip(self.goods, self.quant)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.goods = self.goods.copy()
        new_cart.quant = self.quant.copy()
        if isinstance(other, ShoppingCart):
            for x, y in other:
                new_cart.add_goods(x, y)
        if isinstance(other, Product):
            new_cart.add_goods(other, 1)
        return new_cart


apple = Product('apple', 1.8)
beers = Product('beers', 5.55555555)
beers2 = Product('beers2', 3.5)
bread = Product('bread', 3.2)
apple2 = Product('apple', 1.8)
