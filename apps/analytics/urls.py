from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_crypto_data, name='ctypto_data'),
]