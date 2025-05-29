import requests
from bs4 import BeautifulSoup

# 1.
url = 'https://parsinger.ru/4.1/1/index4.html'
response  = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def extract_price_sum(html):
    soup = BeautifulSoup(html, 'html.parser')

    prices = soup.find_all('p', class_='product_price')

    total = 0
    for price in prices:
        total += int(price.text[:-4].replace(' ', ''))

    return total


print(extract_price_sum(html))

# 2.
url = 'https://parsinger.ru/4.1/1/index4.html'

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags_li = soup.find_all('li')
    for tag in tags_li:
        print(tag['id'])


get_html(html)

# 3.
url = 'https://parsinger.ru/4.1/1/index6.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    sibling = soup.find('section', id='section3').find('p', class_='section-text').next_sibling.text.strip()

    return sibling


print(get_html(html))

# 4.
url = 'https://parsinger.ru/4.1/1/index5.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    emails_batch = soup.find_all('div', class_='email_field')
    emails = [email.strong.next_sibling.text.strip() for email in emails_batch]

    return emails


print(get_html(html))
