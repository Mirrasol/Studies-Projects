import requests
import time

# 1. Когда нужны задержки для отправки серверу
url = 'http://httpbin.org/'

response = requests.get(url)

if response.status_code != 200:
    time.sleep(60)
else:
    print("status_code OK... Continue execute code...")


# 2. Суммируем коды от многих запросов
url_base = 'https://parsinger.ru/3.3/2/'

result = 0

with requests.Session() as s:
    s.get('https://parsinger.ru')

    start = time.perf_counter()

    for i in range(1, 201):
        response = s.get(f'{url_base}{i}.html')
        code = response.status_code
        result += code
        
    end = time.perf_counter()

print(result)
print(end - start)


# 3. Поиск числа на рабочей ссылке из многих нерабочих
url_base = 'https://parsinger.ru/3.3/1/'

with requests.Session() as s:
    s.get('https://parsinger.ru')

    for i in range(1, 201):
        response = s.get(f'{url_base}{i}.html')
        if response.status_code == 200:
            print(response.text)
            break


# 4. Поиск изображения самого большого размера
url_base = 'https://parsinger.ru/3.3/3/img/'

name_img = []

biggest = 0
result = ''

with requests.Session() as s:
    s.get('https://parsinger.ru')

    for i in name_img:
        response = s.get(f'{url_base}{i}')
        size = int(response.headers.get('Content-Length'))
        if size > biggest:
            biggest = size
            result = i

print(result[:-4])


# 5. Поиск доступных страниц в диапазоне
url_base = 'https://parsinger.ru/3.3/4/'

start = 0
end = 0

with requests.Session() as s:
    s.get('https://parsinger.ru')

    for i in range(1, 101):
        response = s.get(f'{url_base}{i}.html')
        if response.status_code == 200:
            start = i
            break
    for i in range(101, start, -1):
        response = s.get(f'{url_base}{i}.html')
        if response.status_code == 200:
            end = i
            break

print(f'{start}.html')
print(f'{end}.html')
