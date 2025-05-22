import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/3.2/simple_product_page.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
result = soup.select_one('.product .price').text
print(result)
