import requests
from datetime import date, timedelta
from .models import CryptoCoin

API_KEY = '40c0ce82-9eee-4926-80fe-9afe2477ca01' 
def get_general_info():
    url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'       #
    headers = {'X-CMC_PRO_API_KEY': API_KEY}                                        # Получаем данные о монетах с помощью API
    response = requests.get(url, headers=headers)                                   #
    data = response.json()                                                          #

    data_from_db = CryptoCoin.objects.all().order_by('-add_date')[:5]               # Получаем последние добавленные 5 монет

    return data, data_from_db

# def get_7d_prices():
#     API_KEY = '40c0ce82-9eee-4926-80fe-9afe2477ca01'
#     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#     headers = {'X-CMC_PRO_API_KEY': API_KEY}
#     params = {
#         'symbol': "symbol",
#         # 'time-start': (date.today() - timedelta(days=7)).strftime('%Y-%m-%d'),
#         # 'time-end': date.today().strftime('%Y-%m-%d'), 
#         # 'interval': 'daily'
#     }
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()
#     return data


def get_coins_details(id):
    url = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?id={id}'
    url_metadata = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?id={id}'
    headers = {'X-CMC_PRO_API_KEY': API_KEY} 
    response = requests.get(url, headers=headers)
    response_metadata = requests.get(url_metadata, headers=headers)
    data = response.json()
    metadata = response_metadata.json()
    return data, metadata
    