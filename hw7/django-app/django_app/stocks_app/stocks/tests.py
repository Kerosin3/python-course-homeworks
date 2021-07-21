from django.test import TestCase
import math
from .models import Stock

# Create your tests here.
class TestStocks(TestCase):


    def test_sqrt(self):
        self.assertEqual(math.sqrt(4),2)

    def test_stock_creation(self):
        name = 'ABCD'
        print(f'testing testing stock')
        s0 = Stock.create_stock(name)
        self.assertEqual(s0.ticker,name)


    def test_stock_data_creating(self):
        print(f'testing stock data creating')
        s0 = Stock.create_stock()
        self.assertIsNotNone(s0.created_at)
        self.assertIsNotNone(s0.updated_at)




    # def test_stock_creation(self):
    #     name = 'ABCD'
    #     print(f'testing testing stock')
    #     s0 = Stock.create_stock(name)
    #     self.assertEqual(s0.ticker, name)
