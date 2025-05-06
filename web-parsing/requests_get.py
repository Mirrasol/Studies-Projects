import random
import requests
import time

# 1. General Info.
url='http://httpbin.org/'

response = requests.get(url)

# status_code: HTTP-код статуса ответа.
print("HTTP-код статуса ответа:", response.status_code)

# text: Текстовое представление содержимого ответа.
print("Текстовое содержимое ответа:", response.text)

# content: Содержимое ответа в виде байтов.
print("Содержимое ответа в виде байтов:", response.content)

# json: Метод для десериализации JSON-ответа.
json_response = response.json()
print("Десериализованный JSON-ответ:", json_response)

# headers: Заголовки HTTP, возвращаемые сервером.
print("Заголовки HTTP:", response.headers)

# url: Исходный URL-адрес, на который был выполнен запрос.
print("Исходный URL-адрес запроса:", response.url)

# encoding: Кодировка ответа.
print("Кодировка ответа:", response.encoding)

# elapsed: Время, затраченное на выполнение запроса.
print("Время выполнения запроса:", response.elapsed)

# cookies: Куки, возвращаемые сервером.
print("Куки, возвращаемые сервером:", response.cookies)

# history: Список объектов Response, представляющих историю перенаправлений.
print("История перенаправлений:", response.history)

# ok: Логический атрибут, указывающий, был ли запрос успешным (коды 2xx).
print("Запрос успешен (коды 2xx):", response.ok)

# reason: Сообщение статуса HTTP (например, "OK", "Not Found").
print("Сообщение статуса HTTP:", response.reason)


# 2. Маскируем Юзер-Агент

url = 'http://httpbin.org/user-agent'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=my_headers)

print("Отправленные заголовки (User-Agent):")
print(response.json().get('user-agent')) 


# 3. Ротация Юзер-Агента

url = 'http://httpbin.org/user-agent'

# Чтение User-Agent'ов из файла
with open('user_agent.txt') as file:
    # Читаем все строки, убираем пустые строки и пробелы по краям
    user_agents_list = [line.strip() for line in file if line.strip()]

random_user_agent = random.choice(user_agents_list)  # Выбор случайного User-Agent
print(f"Выбран случайный User-Agent: {random_user_agent}")

headers = {'User-Agent': random_user_agent}

response = requests.get(url=url, headers=headers)
response.raise_for_status() # Проверка на HTTP ошибки (4xx, 5xx)

print("Ответ сервера:")
print(response.text)

# В реальных парсерах, которые делают много запросов, стоит также 
# добавлять задержки между запросами time.sleep(random.uniform(1, 5))
# и использовать прокси-серверы для смены IP-адреса.


# 4. Имитируем ошибку от прокси-сервера и таймаут

url = 'http://httpbin.org/get'

proxies = {
    'http': 'http://200.12.55.90:80',
    'https': 'http://200.12.55.90:80'
}
start = time.perf_counter()
try:
    requests.get(url=url, proxies=proxies, timeout=1)
except requests.exceptions.ProxyError as e:
    print(f'wait time = {time.perf_counter() - start}')


# 5.1 Грузим маленький файл

# Выполняем GET-запрос к указанному URL с параметром stream=True.
# Параметр stream=True гарантирует, что соединение будет удерживаться,
# пока не будут получены все данные.
response = requests.get(url=url, stream=True)

# Открываем (или создаем) файл 'file.mp4' в режиме 'wb' (write binary),
# чтобы сохранить в него бинарные данные.
with open('file.mp4', 'wb') as file:

    # Записываем содержимое ответа (response.content) в файл.
    # Этот метод подходит для относительно небольших файлов,
    # так как все содержимое файла сначала загружается в оперативную память.
    file.write(response.content)


# 5.2 Грузим большой файл, кусками

response = requests.get(url=url, stream=True)
with open('file.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)


# 6. Используем параметры

import requests

API_KEY = "7e04c92c44b1421d94b113151250604"

BASE_URL = "http://api.weatherapi.com/v1/current.json"

params = {
    "key": API_KEY,     # API-ключ
    "q": "Moscow",      # Город
    "lang": "ru"        # Язык ответа — русский
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)


# 7. Proxies
# Функция для выполнения запроса с использованием прокси
def make_request(url, proxy):
    try:
        response = requests.get(url=url, proxies=proxy)
        print(response.json())
    except Exception as e:
        print(f"Ошибка: {e}")

# URL для тестирования прокси
url = 'http://httpbin.org/ip'

# Прокси для HTTP и HTTPS
proxy_http_https = {
    'http': 'http://103.177.45.3:80',
    'https': 'https://103.177.45.3:80',
}
make_request(url, proxy_http_https)

# Прокси для SOCKS4
proxy_socks4 = {
    'http': 'socks4://103.177.45.3:80',
    'https': 'socks4://103.177.45.3:80',
}
make_request(url, proxy_socks4)

# Прокси для SOCKS5
proxy_socks5 = {
    'http': 'socks5://103.177.45.3:80',
    'https': 'socks5://103.177.45.3:80',
}
make_request(url, proxy_socks5)

# Если ваш прокси-сервер требует логин и пароль, укажите их прямо в URL прокси:

# Прокси с авторизацией
proxy_with_auth = {
    'http': 'socks5://login:password@103.177.45.3:8000',
    'https': 'socks5://login:password@103.177.45.3:8000',
}
make_request(url, proxy_with_auth)
