import requests
from bs4 import BeautifulSoup

# 8.
url = 'https://parsinger.ru/4.3/5/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def calculate_total_price(html: str) -> float:
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all(class_='book-card')

    total = 0.00

    for book in books:
        book_price = book.find(class_='count price').text[7:]
        book_amount = book.find(class_='count stock').text[22:]
        total += float(book_price) * float(book_amount)
    
    return total

print(f"Общая стоимость в случае продажи всех товаров: ${calculate_total_price(html):.2f}")

# 9.
url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
prices = soup.find_all(class_='price')
total = 0
for price in prices:
    total += int(price.text[:-4])
print(total)

# 10.
url = 'http://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
price_old = soup.find(id='old_price').text[:-4]
price_new = soup.find(id='price').text[:-4]
discount = (int(price_old) - int(price_new)) * 100 / int(price_old)
print(f'{discount:.1f}')
