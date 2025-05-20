import requests
from bs4 import BeautifulSoup

# 1. Basics
url = 'http://parsinger.ru/html/watch/1/1_1.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


# 2. Tags
# Наш HTML-код в виде строки
html_doc = """
<html>
    <head>
        <title>Мой Супер Сайт</title>
    </head>
    <body>
        <div class="content">
            <p>Привет, мир парсинга! 👋</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')  # cоздаем объект BeautifulSoup, указываем парсер

title_tag = soup.title  # работаем с тегом title
print(f"🏷️Текст из тега title: {title_tag.text}")
print(f"📝Имя тега: {title_tag.name}") 

p_tag = soup.p  # работаем с тегом <p>
print(f"✍️Текст из тега p: {p_tag.text}")


# 3. Скачиваем в файл для локальной работы.
url = 'http://parsinger.ru/html/watch/1/1_1.html'

response = requests.get(url)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
