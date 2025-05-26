import requests
from bs4 import BeautifulSoup

# 1.
url = 'http://31.130.149.237/api/v1/ajax/GetSum'

data = {
    'GiveName': 'JPY',
    'GetName': 'DOGE',
    'Sum': 51284.43,
    'Direction': '0',
}

response = requests.get(url=url, params=data)
print(response.text)


# 2.
url = 'http://31.130.149.237/api/v1/ajax/GetSum'

amounts_per_give_currency = {
        "USD": 150, "EUR": 120, "RUB": 20000, "BYN": 50, "JPY": 50000,
        "GBP": 250, "CAD": 1000, "BTC": 0.01, "ETH": 0.5, "SOL": 10,
        "USDT": 150, "ADA": 300, "DOGE": 5000, "XRP": 1000, "BNB": 1,
        "USDC": 150, "TRX": 10000
}

data = {
    'GiveName': key1,
    'GetName': key2,
    'Sum': value,
    'Direction': '0',
}

response = requests.get(url=url, params=data)
