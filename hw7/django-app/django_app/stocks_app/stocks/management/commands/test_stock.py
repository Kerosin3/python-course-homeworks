from django.core.management import BaseCommand
from stocks.models import Stock,Prices  # not stocks.models
from stocks.models import Misc


class Command(BaseCommand):

    def handle(self, *args, **options):
        Stock.objects.all().delete()
        print('creating a test stock')
        stock = Stock.objects.create(ticker='TEST',
                                     current_price=666.6,
                                     comment='test comment')
        print(stock.ticker)
        print(stock.current_price)
        # prices = Prices.objects.create(value_price=111,
        #                                key_data= '11.11.11')
        # print(prices.value_price)
        print(stock.prices) # None type !!
        # stock.prices.key_data = '11.12.13' ....
        # stock.save() ...

