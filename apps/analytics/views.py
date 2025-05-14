from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET']) # Разрешаем только GET запросы
def get_crypto_data(request):

    return render(request, 'analytics/index.html')

def fetch_crypto_api(request):
    url = 'https://api.coinlore.net/api/ticker/?id=90'
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({"error": "Ошибка при получении данных"}, safe=False)
    return JsonResponse(response.json(), safe=False)
    
    
