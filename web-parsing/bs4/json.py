import requests
from bs4 import BeautifulSoup
import json

url = 'http://parsinger.ru/html/mouse/3/3_11.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

result_json = {
    'name': soup.find('p', id='p_header').text,
    'price': soup.find('span', id='price').text}

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
