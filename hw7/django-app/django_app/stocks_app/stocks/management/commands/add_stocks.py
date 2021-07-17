from django.core.management import BaseCommand
from stocks.models import Stock, Prices, Financials


# from stocks.models import Misc


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Stock.objects.all().delete()
        # Prices.objects.all().delete()
        # Financials.objects.all().delete()
        # Prices.objects.all().delete()
        print('======================')
        for i in range(5):
            S0 = Stock.create_stock()
            S0.add_n_prices(10)
            S0.get_full_info()
        print('======================')
