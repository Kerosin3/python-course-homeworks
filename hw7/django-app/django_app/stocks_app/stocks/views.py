from django.http import Http404
from django.shortcuts import render
from .models import Stock
import time
from .tasks import save_stocks_task
from django.core.mail import send_mail
# Create your views here.


def index_page(request):
    a_stock = Stock.objects.all()
    if a_stock is not None and request.method == 'GET':
        #nothing
        print('used get method')
    elif a_stock is not None and request.method == 'POST': # POST
        save_stocks_task.delay()
    else:
        raise Http404
    return render(request, 'stocks/index.html',{'stocks':a_stock})
