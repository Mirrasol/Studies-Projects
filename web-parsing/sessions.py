import requests
import time
from itertools import cycle

# 1. Session Example
session = requests.Session()

response = session.get('https://httpbin.org/get')
print(response.status_code)

response2 = session.get('https://httpbin.org/get')
print(response2.status_code)

session.close()


# 2. Замеряем время сессии
with requests.Session() as session:
    start_time = time.time()
    for _ in range(10):
        response = session.get('https://example.com')
    end_time = time.time()

    print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')


# 3. Аутентификация на прокси
url = "https://httpbin.org/ip"

proxies = {
    'http': 'socks5://8ZYk5H:XfMpg7@10.10.36.159:8000',
    'https': 'socks5://Kx4Jcj:h4Ch0N@10.10.51.205:8000',
}

session = requests.Session()

session.proxies.update(proxies)

response = session.get(url)

print(response.text)


# 4. Автоматом переключаем прокси
proxies_list = [
    {'http': 'http://10.10.36.159:8000', 'https': 'https://10.10.36.159:8000'},
    {'http': 'http://10.10.51.205:8000', 'https': 'https://10.10.51.205:8000'},
    {'http': 'http://10.10.79.216:8000', 'https': 'https://10.10.79.216:8000'},
    # ... и так далее
]

# Создаём бесконечный итератор, который по кругу перебирает элементы из списка proxies_list:
proxy_pool = cycle(proxies_list)

url = "http://example.org"

session = requests.Session()

for i in range(1, 6):
    proxy = next(proxy_pool)       # Берём следующий прокси из "пула", по кругу
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")
