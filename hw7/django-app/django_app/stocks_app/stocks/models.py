from django.db import models
from datetime import date

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=4,unique=True)
    current_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
