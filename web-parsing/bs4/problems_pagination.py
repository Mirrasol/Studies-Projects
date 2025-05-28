import requests
import lxml
from bs4 import BeautifulSoup

# 1.
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


# 2.
url = 'http://stepik-parsing.ru/html/index3_page_1.html'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
pagen = [int(x.text) for x in soup.find('div', class_='pagen').find_all('a')][-1]

link_all = []
for i in range(1, pagen+1):
    url = f'http://stepik-parsing.ru/html/index3_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link = soup.find_all('a', class_='name_item')
    for x in link:
        link_all.append(f"http://stepik-parsing.ru/html/{x['href']}")


result = []
for url in link_all:
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find('p', class_='article').text.split(':')[1]
    result.append(int(article))
print(sum(result))
