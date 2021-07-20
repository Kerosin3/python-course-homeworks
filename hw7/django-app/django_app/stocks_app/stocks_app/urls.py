"""stocks_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stocks.views import status_view, home_view, StockListView, StockDetailsView, CreateStockView,RemoveStocksView,UpdateStockView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_page),
    path('', StockListView.as_view()),
    path('stock/<int:pk>/', StockDetailsView.as_view()),
    path('stock/remove/<int:pk>/', RemoveStocksView.as_view()),
    path('task/', status_view),
    path('home/', home_view),
    path('stock/update/<int:pk>/', UpdateStockView.as_view()),
    # path('add_stocks/', add_stocks_view),
    path('add_stocks/', CreateStockView.as_view(),
    )
]
