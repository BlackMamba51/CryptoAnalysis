import requests
from datetime import date, timedelta
import os



def get_7d_prices():
    API_KEY = '40c0ce82-9eee-4926-80fe-9afe2477ca01'
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {'X-CMC_PRO_API_KEY': API_KEY}
    params = {
        'symbol': "symbol",
        # 'time-start': (date.today() - timedelta(days=7)).strftime('%Y-%m-%d'),
        # 'time-end': date.today().strftime('%Y-%m-%d'), 
        # 'interval': 'daily'
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data