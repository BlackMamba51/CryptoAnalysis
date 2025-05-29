from django.db import models

class CryptoCoin(models.Model):
    coin_name = models.CharField(max_length=15)
    coin_symbol = models.CharField(max_length=5)
    coin_price = models.PositiveIntegerField()
    coin_count = models.PositiveIntegerField()
