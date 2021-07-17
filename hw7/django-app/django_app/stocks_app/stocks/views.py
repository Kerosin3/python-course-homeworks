from django.http import Http404
from django.shortcuts import render
from .models import Stock
import time
from .tasks import save_stocks_task,send_mail_task
from celery import current_app
# Create your views here.


def index_page(request):
    a_stock = Stock.objects.all()
    task_id = None
    if a_stock is not None and request.method == 'GET':
        #nothing
        print('used get method')
    elif a_stock is not None and request.method == 'POST': # POST
        # save_stocks_task.delay()
        a_task = send_mail_task.delay('testSBJ','SOMEtexttt')
        task_id = a_task.id

    else:
        raise Http404
    return render(request, 'stocks/index.html',{'stocks':a_stock,
                                                'task_id':task_id})

def status_view(request):
    task_id = request.GET['task_id']
    task = current_app.AsyncResult(task_id) #task's data
    status = task.status
    print('status is !!!!', status)
    print('task id is',task_id)
    return render(request, 'stocks/status_view.html',
                  {'task_id':task_id,
                  'status':status})
