import requests
from bs4 import BeautifulSoup

url = f'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


soup = BeautifulSoup(html, 'html.parser')
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

result = []

for i in range(4):
    url_page = f'https://parsinger.ru/html/{pagen[i]}'
    response = requests.get(url_page)
    response.encoding = 'utf-8'
    html_page = response.text

    soup = BeautifulSoup(html_page, 'html.parser')

    items = soup.find_all('a', class_='name_item')
    page = [item.text for item in items]
    result.append(page)

print(result)
