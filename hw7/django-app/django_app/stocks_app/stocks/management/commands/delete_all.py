from django.core.management import BaseCommand
from stocks.models import Stock  # not stocks.models

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('hello command')
        Stock.objects.all().delete()

