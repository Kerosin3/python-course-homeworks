from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import time
from collections import OrderedDict

#current financials
class Financials(models.Model):
    pe = models.FloatField(default=0.0)
    pb = models.FloatField(default=0.0)
    mar_cap = models.FloatField(default=0.0)

class Prices(models.Model):
    # prices = OrderedDict()
    prices = models.FloatField()
    # stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Stock(models.Model):
    ticker = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')]
                              ,unique=True,max_length=4)
    current_price = models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        blank=True,
                                        null=True,
                                        default=0.0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    comment = models.TextField(blank=True)
    prices = models.ForeignKey(Prices, on_delete=models.CASCADE)
    financials = models.ForeignKey(Financials, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

class Sector(models.Model):
    #enumerate it
    sector = models.CharField(max_length=20,unique=False)
    stock = models.OneToOneField(Stock,on_delete=models.PROTECT)

class Misc():

    @staticmethod
    def get_cur_data():
        #14/07/2021:15:23:09.930 format
        time.sleep(0.05)
        now = datetime.now()
        return (now.strftime("%d/%m/%Y:%H:%M:%S.%f")[:-3])
