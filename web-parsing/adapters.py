import requests
from requests.adapters import HTTPAdapter
from itertools import cycle

# 1. Адаптер в целом
session = requests.Session()

# Создаем адаптер с конфигурацией по умолчанию
adapter = HTTPAdapter(pool_connections=10, pool_maxsize=20)

# Монтируем адаптер для HTTP и HTTPS
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get('https://httpbin.org/get')
print(response.status_code)  # 200


# 2. Адаптер + прокси
import requests
from requests.adapters import HTTPAdapter
from itertools import cycle

proxies_list = [
    {"http": "http://10.10.1.11:3128", "https": "socks5://10.10.10.11:3128"},
    {"http": "socks5://10.10.10.159:8000", "https": "socks5://10.10.10.159:8000"},
        #...
    {"http": "socks5://10.10.10.216:8000", "https": "socks5://10.10.10.216:8000"},
]

session = requests.Session()

def make_request(proxy):
    adapter = HTTPAdapter(
        pool_connections=10,
        pool_maxsize=20,
        max_retries=5
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get('https://httpbin.org/get', proxies=proxy, timeout=5)
        print(f'Успех с прокси {proxy}: {response.status_code}')
        return True
    except requests.exceptions.RequestException as e:
        print(f'Не удалось использовать прокси {proxy}: {str(e)}')
        return False
           

# Используем cycle, чтобы «карусель» прокси не заканчивалась.
proxy_pool = cycle(proxies_list)     # Бесконечный итератор

# Перебор прокси и запросов
proxy_index = 0
for _ in range(5):
    proxy = next(proxy_pool)   
    if make_request(proxy):
        break                        # Если запрос успешен — выходим из цикла
    # Если неудача, попробуем сразу следующий прокси
    if make_request(next(proxy_pool)):
        break

session.close()
