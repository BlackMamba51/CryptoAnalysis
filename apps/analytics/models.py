from django.db import models
from datetime import date
class CryptoCoin(models.Model):
    coin_name = models.CharField(max_length=15)
    coin_symbol = models.CharField(max_length=5)
    coin_price = models.PositiveIntegerField()
    coin_count = models.PositiveIntegerField()
    add_date = models.DateField(default=date.today)
