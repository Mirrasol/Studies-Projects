from bs4 import BeautifulSoup

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
