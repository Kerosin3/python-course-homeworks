import random

from django.core.validators import RegexValidator
from django.db import models
from .models_misc import get_rand_data, get_cur_data, gen_ticker


# current financials
class Financials(models.Model):
    pe = models.FloatField(default=0.0, null=True)
    pb = models.FloatField(default=0.0, null=True)
    # mar_cap = models.FloatField(default=0.0)


class Stock(models.Model):
    count: int = 0

    id = models.AutoField(primary_key=True)
    ticker = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')]
                              , unique=True, max_length=4)
    current_price = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        blank=False,
                                        null=True,
                                        default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    finances = models.OneToOneField(Financials, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.ticker

    def __repr__(self):
        return f'stock ticker is {self.ticker},' \
               f'current price is {self.current_price}'
        # f'and p/e is {self.financials.pe},' \
        # f'p/b is {self.financials.pb},' \
        # f'record date is {self.created_at},' \

    @classmethod
    def create_stock(cls):
        fin = Financials.objects.create(
            pe=get_rand_data(),
            pb=get_rand_data(),
        )
        stock_temp = Stock.objects.create(
            ticker=gen_ticker(),
            current_price=get_rand_data(),
            comment='comment aaa',
            finances=fin
        )
        cls.count += 1
        stock_temp.save()  # save the stock
        print('a stock template has been created (no price at this day)')
        return stock_temp

    def add_n_prices(self, n_prices: int = 1):
        Prices().add_n_prices(self, n_prices)
        print(f'------added {n_prices} prices------')

    def show_all_prices(self):  # self if STOCK!!
        # get all prices
        pricess = self.prices_set.all()
        for pr in pricess:
            print(f'Stock {self.ticker} '
                  f'at date :{pr.key_data},'
                  f'price was {pr.value_price},'
                  f' id={pr.id}')

    def get_full_info(self):
        print(f'Stock ticker: {self.ticker},'
              f' it\'s current price is {self.current_price}'
              f' it\'s P\E is {self.finances.pe}, '
              f'and P\B is {self.finances.pb}')
        pricess = self.prices_set.all()
        for pr in pricess:
            print(f'Stock {self.ticker} '
                  f'at date :{pr.key_data},'
                  f'price was {pr.value_price},'
                  f' id={pr.id}')


class Prices(models.Model):
    id = models.AutoField(primary_key=True)
    value_price = models.FloatField(default=0.0, db_index=True)
    key_data = models.CharField(max_length=50,
                                default='TEST_DATA',
                                db_index=True)
    objects_stocks = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=False, null=True)

    @staticmethod
    def add_price(a_stock: Stock):
        p0 = Prices.objects.create(
            value_price=get_rand_data(),
            key_data=get_cur_data(),
            objects_stocks=a_stock
        )
        p0.save()  # save a price

    @staticmethod
    def add_n_prices(a_stock: Stock, n: int = 1):
        for i in range(n):
            p0 = Prices.objects.create(
                value_price=get_rand_data(),
                key_data=get_cur_data(),
                objects_stocks=a_stock
            )
            p0.save()  # save n'th price
