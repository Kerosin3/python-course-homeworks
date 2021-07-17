import time
from .models import Stock
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def save_stocks_task():
    time.sleep(3)
    a_stock = Stock.objects.all()
    with open('data_tickers.txt', 'w', encoding='utf-8') as filex:
        for stock in a_stock:
            filex.write(stock.ticker + '\n')

@shared_task()
def send_mail_task(subject:str='Subject here',
                   message:str='Here is the message.'):
    time.sleep(5)
    send_mail(subject,message ,
              'from@example.com',
              ['to@example.com'],
              fail_silently=False)
