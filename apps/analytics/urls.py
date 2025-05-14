from django.urls import path

from .views import fetch_crypto_api, get_crypto_data

urlpatterns = [
    path("api/crypto/", fetch_crypto_api, name='crypto_api'),
    path("", get_crypto_data, name='crypto_data'),
]