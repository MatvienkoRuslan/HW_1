

class ShoppingCart:
    def __init__(self,*goods):
        self.goods = goods

    def pay(self) -> float:
        return f'Total cost is {sum(self.goods):.2f} leafs.'
        c1 = ShoppingCart(apple.total_cost(3), cheese.total_cost(2))