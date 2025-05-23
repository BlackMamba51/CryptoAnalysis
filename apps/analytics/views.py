from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests, os

from .utils import get_general_info

@api_view(['GET']) # Разрешаем только GET запросы
def get_crypto_data(request):
    data = get_general_info()
    return render(request, 'analytics/index.html', {'data': data})



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