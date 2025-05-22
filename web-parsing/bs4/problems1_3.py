import lxml
import requests
from bs4 import BeautifulSoup

# 1.
path = 'index.html'

with open(path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

print(soup)

# 2.
url = 'https://parsinger.ru/4.1/1/index3.html'
response = requests.get(url)
html = response.text

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})

    print(tag.text) 


get_html(html)

# 3.
html = """
<div>
    <p class="first">Первый абзац.</p>
    <p class="first second">Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find_all('p', class_='first')
    for i in tag:
        print(i) 


get_html(html)
