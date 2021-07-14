from django.http import Http404
from django.shortcuts import render
from .models import Stock
# Create your views here.


def index_page(request):
    if request.method == 'GET':
        a_stock = Stock.objects.all()
    else:
        raise Http404
    return render(request, 'stocks/index.html',{'stocks':a_stock})
