from django.urls import path

from .views import fetch_crypto_api, get_crypto_data, add_crypto, add_coin, coin_detail

urlpatterns = [
    path("api/crypto/", fetch_crypto_api, name='crypto_api'),
    # path("api/binance/", crypto_chart, name='binance_api'),
    path("", get_crypto_data, name='crypto_data'),
    path("coin_detail/<int:coin_id>/", coin_detail, name='coin_detail'),
    path("add_crypto/", add_crypto, name='add_crypto'),
    path("add_crypto/add_coin/", add_coin, name='add_coin'),
]