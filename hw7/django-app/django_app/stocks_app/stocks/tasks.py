import time
from .models import Stock
from celery import shared_task


@shared_task
def save_stocks_task():
    time.sleep(3)
    a_stock = Stock.objects.all()
    with open('data_tickers.txt', 'w', encoding='utf-8') as filex:
        for stock in a_stock:
            filex.write(stock.ticker + '\n')
