from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import time
from collections import OrderedDict

class Financials(models.Model):
    pe = models.FloatField()
    pb = models.FloatField()
    mar_cap = models.FloatField()

class Prices(models.Model):
    # prices = OrderedDict()
    prices = models.FloatField()
    # stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Stock(models.Model):
    ticker = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')]
                              ,unique=True)
    current_price = models.DecimalField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    comment = models.TextField(blank=True)
    financials = models.ForeignKey(Financials, on_delete=models.CASCADE)
    prices = models.ForeignKey(Prices, on_delete=models.CASCADE)


    def __str__(self):
        return self.ticker

class Sector(models.Model):
    #enumerate it
    sector = models.CharField(max_length=20,unique=False)
    stock = models.OneToOneField(Stock,on_delete=models.PROTECT)


def get_cur_data():
    #14/07/2021:15:23:09.930 format
    time.sleep(0.05)
    now = datetime.now()
    return (now.strftime("%d/%m/%Y:%H:%M:%S.%f")[:-3])
