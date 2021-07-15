import random

from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import time
from enum import Enum, unique
import string
from collections import OrderedDict


# current financials
class Financials(models.Model):
    pe = models.FloatField(default=0.0)
    pb = models.FloatField(default=0.0)
    # mar_cap = models.FloatField(default=0.0)


class Prices(models.Model):
    value_price = models.FloatField(default=0.0, db_index=True)
    key_data = models.CharField(max_length=50,
                                default='TEST_DATA',
                                db_index=True)


class Laying(models.Model):
    id = models.AutoField(primary_key=True)
    container = models.ForeignKey(Prices, db_index=True, on_delete=models.CASCADE)


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')]
                              , unique=True, max_length=4)
    current_price = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        blank=True,
                                        null=True,
                                        default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    comment = models.TextField(blank=True)
    prices = models.OneToOneField(Laying, on_delete=models.CASCADE, blank=True, null=True)
    financials = models.ForeignKey(Financials, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ticker

    def __repr__(self):
        return f'stock ticker is {self.ticker},' \
               f'and p/e is {self.financials.pe},' \
               f'p/b is {self.financials.pb},' \
               f'record date is {self.created_at},' \
               f'current price is {self.current_price}'


class Sector(models.Model):
    # enumerate it
    sector = models.CharField(max_length=20, unique=False)
    stock = models.OneToOneField(Stock, on_delete=models.PROTECT, blank=True, null=True)


class Misc():
    @staticmethod
    def get_cur_data():
        # 14/07/2021:15:23:09.930 format
        time.sleep(0.05)
        now = datetime.now()
        return (now.strftime("%d/%m/%Y:%H:%M:%S.%f")[:-3])

    @staticmethod
    def get_rand_data():
        return round(random.uniform(0, 200), 3)

    @staticmethod
    def gen_ticker():
        return ''.join(random.sample(string.ascii_uppercase, 4))

    @unique
    class Sectors(Enum):
        TESTsector = 0,
        Financials_and_Banks = 1,
        IT = 2,
        Hardware = 3,
        Industry = 4,
        Energy = 5,
        Commodies = 6,

    @staticmethod
    def fill_prices() -> Laying:
        l0 = Laying()
        p0 = None
        for i in range(0, 5):
            p0 = Prices()
            p0.value_price = Misc.get_rand_data()
            p0.key_data = Misc.get_cur_data()
            p0.save()
            l0.container = p0
            print(f'create price {p0.value_price} '
                  f'with data {p0.key_data}')
        l0.save()
        return l0

    @staticmethod
    def create_stock():
        p0 = Prices(value_price=Misc.get_rand_data(),
                    key_data=Misc.get_cur_data())
        p0.save()
        f0 = Financials(pe=Misc.get_rand_data(),
                        pb=Misc.get_rand_data())
        f0.save()
        stock = Stock.objects.create(ticker=Misc.gen_ticker(),
                                     current_price=Misc.get_rand_data(),
                                     comment='test comment',
                                     prices=p0,
                                     financials=f0,
                                     )
        sec = Misc.Sectors.TESTsector.name
        s0 = Sector(sector=sec,
                    stock=stock)

        return stock

    @staticmethod
    def create_stockv2():
        # p0 = Prices(value_price=Misc.get_rand_data(),
        #             key_data=Misc.get_cur_data())
        # p0.save()
        f0 = Financials(pe=Misc.get_rand_data(),
                        pb=Misc.get_rand_data())
        f0.save()
        stock = Stock.objects.create(ticker=Misc.gen_ticker(),
                                     current_price=Misc.get_rand_data(),
                                     comment='test comment',
                                     financials=f0,
                                     prices=Misc.fill_prices()
                                     )

        # Prices = Misc.fill_prices(stock)
        sec = Misc.Sectors.TESTsector.name
        s0 = Sector(sector=sec,
                    stock=stock)

        return stock
