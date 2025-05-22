import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.1/1/index3.html'
response = requests.get(url)
html = response.text

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})

    print(tag.text) 


get_html(html)
