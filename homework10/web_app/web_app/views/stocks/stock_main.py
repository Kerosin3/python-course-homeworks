from dataclasses import dataclass
from random import randint


def gen_stock_prices(n: int = 10):
    list_prices = []
    for i in range(n):
        list_prices.append(randint(0, 55))
    return sum(list_prices)


@dataclass
class Stock:
    ticker: str
    price: int = 0

    def add_price(self, price: int = 0):
        self.price.append(price)

    def get_price(self):
        return self.price[-1]
