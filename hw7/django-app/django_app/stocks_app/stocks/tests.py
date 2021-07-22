import django.db.utils
from django.test import TestCase, TransactionTestCase
import math
from .models import Stock, Prices
from .models_misc import get_rand_data, get_cur_data, gen_ticker


class TestStocks(TransactionTestCase):

    def setUp(self):
        self.name = 'ABCD'
        self.s0 = Stock.create_stock(self.name)
        self.p0 = Prices.objects.create(
            value_price=get_rand_data(),
            key_data=get_cur_data(),
            objects_stocks=self.s0
        )

    def tearDown(self):
        # https://stackoverflow.com/questions/43978468/django-test-transactionmanagementerror-you-cant-execute-queries-until-the-end
        self.p0.delete()
        pricess = len(self.s0.prices_set.all())
        self.assertEqual(pricess, 0)

    def test_stock_creation(self):
        print(f'testing testing stock')
        self.assertEqual(self.s0.ticker, self.name)

    def test_stock_same_name(self):
        name2 = 'ABCD'
        print(f'testing testing stocks with the same name')
        with self.assertRaises(django.db.utils.IntegrityError):
            s1 = Stock.create_stock(name2)

    #
    #
    #
    def test_stock_data_creating(self):
        print(f'testing stock data creating process')
        self.assertIsNotNone(self.s0.created_at)
        self.assertIsNotNone(self.s0.updated_at)

    def test_price(self):
        self.assertEqual(type(self.p0.value_price), float)
        self.assertEqual(type(self.p0.key_data), str)
        self.assertEqual(self.p0.objects_stocks.ticker,
                         self.s0.ticker)
