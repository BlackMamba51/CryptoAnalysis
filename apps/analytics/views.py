from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

def get_crypto_data(request):
    url = ' https://api.coinlore.net/api/ticker/?id=90'

    response = requests.get(url)
    data = response.json()
    data = data[0]
    data_of_coin = {
        'coin': data['name'],
        'symbol': data['symbol']
    }
    return render(request, 'analytics/index.html', {'data': data_of_coin})

