from django.core.management import BaseCommand
from stocks.models import Stock, Prices, Financials, Sector  # not stocks.models
from stocks.models import Misc


class Command(BaseCommand):

    def handle(self, *args, **options):
        Stock.objects.all().delete()
        Prices.objects.all().delete()
        Financials.objects.all().delete()

        print('creating a test stock')
        s0 = Misc.create_stockv2()
        print(s0.__repr__())
        print(s0.prices.container.value_price)
        print(s0.prices.container.key_data)
        # print(s0.prices.Laying)
