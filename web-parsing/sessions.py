import requests
import time

# 1. Session Example
session = requests.Session()

response = session.get('https://httpbin.org/get')
print(response.status_code)

response2 = session.get('https://httpbin.org/get')
print(response2.status_code)

session.close()


# 2. Замеряем время сессии
session = requests.Session()

# Измерение времени выполнения запросов с переиспользованием соединения
start_time = time.time()
for _ in range(10):
    response = session.get('https://example.com')
end_time = time.time()

print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')