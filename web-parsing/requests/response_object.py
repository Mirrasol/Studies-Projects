import requests
import ijson

# 1. JSON для больших данных.
response = requests.get("https://api.example.com/large_data", stream=True)
response.url
parser = ijson.parse(response.raw)
for prefix, event, value in parser:
     # Обработка данных
     pass


# 2. Качаем изображения с сайта
url = 'http://parsinger.ru/img_download/img/ready/'

for i in range(1, 161):
    response = requests.get(f'{url}{i}.png')
    with open(f'/home/mirrasol/pics/{i}.png', 'wb') as file:
        file.write(response.content)


# 3. Погода API
API = 'https://parsinger.ru/3.4/1/json_weather.json'

response = requests.get(API).json()

def get_int_temperature(str_temperature):
    result = int(str_temperature.strip('°C'))
    return result


min_temperature = 100
result_date = ''

for item in response:
    current_temperature = get_int_temperature(item['Температура воздуха'])

    if current_temperature < min_temperature:
        min_temperature = current_temperature
        result_date = item['Дата']

print(result_date)


# 4. Вывод HTML

url = 'https://parsinger.ru/3.4/2/index.html'

response = requests.get(url)
response.encoding = 'utf-8'

print(response.text)


# 5. Дерево JSON

API = 'https://parsinger.ru/3.4/3/dialog.json'

response = requests.get(API).json()

users = {}

def get_users(data, users_dict):
    current_user = data.get('username', 0)
    if current_user in users_dict:
        users_dict[current_user] += 1
    else:
        users_dict[current_user] = 1
    
    if data['comments']:
        for comment in data['comments']:
            get_users(comment, users_dict)


get_users(response, users)

sorted_result = {k: v for k, v in sorted(users.items(), key=lambda x: (-x[1], x[0]))}

print(sorted_result)
