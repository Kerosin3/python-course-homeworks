import django.db.utils
from django.test import TestCase, Client
from .models import Stock


class TestViews(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # get ok

    def test_context_null(self):
        response = self.client.get('/')
        self.assertEqual(len(response.context['object_list']), 0)  # get

    def test_context_not_null(self):
        n = 2 # creating 2 Stocks
        for i in range(n):
            S0 = Stock.create_stock()
            S0.add_n_prices(10)
        response = self.client.get('/')
        self.assertEqual(len(response.context['object_list']), n)  # get

    def test_delete_stock(self):
        S0 = Stock.create_stock()
        id = S0.id
        stock_to_del = '/stock/remove/' + str(id) + '/'
        response = self.client.get(stock_to_del)
        self.assertEqual(response.status_code, 200)

class TestTemplates(TestCase):

    def test_content(self):
        response = self.client.get('/')
        text0 = b'navbar'
        self.assertIn(text0, response.content)

    def test_content_base_template_basic(self):
        response = self.client.get('/')
        self.assertIn(b'Add a stock', response.content)
