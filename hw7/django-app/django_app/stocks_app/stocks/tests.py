from django.test import TestCase
import math


# Create your tests here.
class TestStocks(TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(4),2)

