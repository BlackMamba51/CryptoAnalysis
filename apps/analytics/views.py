from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import CryptoCoin
from rest_framework.decorators import api_view
import requests
from .utils import get_general_info


# -- Для шаблона index.html --
@api_view(['GET']) # Разрешаем только GET запросы
def get_crypto_data(request):
    data, data_from_db = get_general_info()
    return render(request, 'analytics/index.html', {'data': data, 'db_data': data_from_db})

def fetch_crypto_api(request):
    API_KEY = '40c0ce82-9eee-4926-80fe-9afe2477ca01'
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    # url_graph = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {'X-CMC_PRO_API_KEY': API_KEY}
    response = requests.get(url, headers=headers)
    # response_url = requests.get(url_graph, headers=headers)
    data = response.json()
    #data_for_graphs = get_7d_prices(data['data'])
    if response.status_code != 200:
        return JsonResponse({"error": "Ошибка при получении данных"}, safe=False)
    return JsonResponse(data['data'], safe=False)
    
# def crypto_chart(request):
#     data = get_7d_prices()
   
#     return JsonResponse(data, safe=False)
# def render_general_info(request):
#     data = get_general_info()
#     return render(request, 'analytics/index.html', {'data': data}) 

# -- Для шаблона index.html --


# -- Для шаблона add_crypto.html --

def add_crypto(request):
    return render(request, 'analytics/add_crypto.html')

def add_coin(request):
    CryptoCoin.objects.create(coin_name=request.POST.get('coin-name'), 
                              coin_symbol=request.POST.get('coin-symbol'), 
                              coin_price=request.POST.get('coin-price'), 
                              coin_count=request.POST.get('coin-count'))
    coin_name = request.POST.get('coin-name')
    coin_symbol = request.POST.get('coin-symbol')
    coin_price = request.POST.get('coin-price')
    coin_count = request.POST.get('coin-count')
    return HttpResponse(f'<h2>{coin_name}({coin_symbol})</h2>')

# -- Для шаблона add_crypto.html -- 