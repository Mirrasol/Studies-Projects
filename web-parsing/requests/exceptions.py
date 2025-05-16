import logging
import requests
import time

# 1. Частые исключения
common_e = [
    requests.exceptions.Timeout,
    requests.exceptions.HTTPError,
    requests.exceptions.ConnectionError,
    AttributeError,
    Exception,
]

# 2. Используем логи для отладки
logging.basicConfig(filename='parser.log', level=logging.ERROR)

url = ''

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logging.error(f"Ошибка при запросе {url}: {e}")

# 4. Добавляем попытки на случай таймаутов и тд
for attempt in range(3):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        break  # Успех, выходим из цикла
    except requests.exceptions.Timeout:
        print(f"Попытка {attempt + 1} не удалась, пробуем снова...")
        time.sleep(2)  # Ждём 2 секунды перед повтором
else:
    print("Все попытки исчерпаны!")


# 5. Проверяем наличие элементов перед доступом к ним
title_tag = soup.find('h1', class_='article-title')
if title_tag:
    title = title_tag.text.strip()
else:
    print("Заголовок не найден!")
