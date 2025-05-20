import lxml
from bs4 import BeautifulSoup

path = 'index.html'

with open(path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

print(soup)
