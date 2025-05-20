import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/object_soup/index.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(type(soup))

p_tag = soup.body.p  # тег <p> из тега <body>

div_tag = soup.div  # первый тег <div>
print(div_tag.name, div_tag.attrs, div_tag.string)
