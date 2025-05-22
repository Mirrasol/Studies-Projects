import requests
from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пример карточки товара</title>
</head>
<body>
    <div class="card">
        <img src="image.jpg" alt="Пример изображения товара">
        <h2 class="card-title"> iPhone 15 </h2>
        <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей. </p>
        <p class="card-price">999 999 руб.</p>
        <a href="https://example.com/product-link" class="card-link">Подробнее</a>
    </div>
</body>
</html>
'''

html_doc = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <div class="cards">
        <!-- Карточка товара 1 -->
        <div class="card">
            <img src="parsing.png" alt="WEB Парсинг на Python">
            <h2 class="card-title">WEB Парсинг на Python</h2>
            <p class="card-articul">Артикул: 104774</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 2 -->
        <div class="card">
            <img src="async.png" alt="Асинхронный Python">
            <h2 class="card-title">Асинхронный Python</h2>
            <p class="card-articul">Артикул: 170777</p>
            <p class="card-stock">Наличие: 10 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 3 -->
        <div class="card">
            <img src="selenium.PNG" alt="Selenium Python">
            <h2 class="card-title">Selenium Python</h2>
            <p class="card-articul">Артикул: 119495</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">1250 руб.</p>
            <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
        </div>
    </div>
</body>
</html>
'''

def main1():
    soup = BeautifulSoup(html, 'html.parser')
    p_description = soup.find('p', class_='card-description').text
    print(p_description)


def main2():    
    soup = BeautifulSoup(html_doc, 'html.parser')
    articuls = [i.text[9:] for i in soup.find_all('p', class_='card-articul')]
    sum_articuls = sum(map(int, articuls))

    print(f"Сумма артикулов: {sum_articuls}")
