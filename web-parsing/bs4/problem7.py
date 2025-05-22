import requests
from bs4 import BeautifulSoup

html_doc = ''''''

url = 'https://parsinger.ru/4.3/4/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text


def main1():
    soup = BeautifulSoup(html_doc, 'html.parser')

    img_tags = soup.find_all('img')

    total_sum = sum([int(i['alt']) for i in img_tags])

    print(f"Сумма всех значений в атрибуте alt тега img: {total_sum}")


def sum_even_length_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    p_tags = soup.find_all('p')
    filtered_tags = list(filter(lambda x: len(x.text.replace(' ', '')) % 2 == 0, p_tags))

    total_id_sum = sum([int(i['id']) for i in filtered_tags])
    total_class_sum = sum([int(i['class'][0]) for i in filtered_tags])

    print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")


sum_even_length_ids(html)
