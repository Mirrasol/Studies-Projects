import asyncio
import requests

import aiohttp
import lxml
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/index1_page_1.html'
domain = 'https://parsinger.ru/html/'

categories = []
pagen = []
result = []


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_categories(soup):
    links = soup.find('div', class_='nav_menu').find_all('a')
    for cat in links:
        categories.append(domain + cat['href'])


def get_urls_pages(categories):
    for cat in categories:
        soup = get_soup(cat)
        for page in soup.find('div', class_='pagen').find_all('a'):
            pagen.append(domain + page['href'])


async def get_data(session, link):
    async with session.get(url=link) as response:
        if response.ok:
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            item_card = [i['href'] for i in soup.find_all('a', class_='name_item')]
            for item_link in item_card:
                card_url = domain + item_link
                async with session.get(url=card_url) as item_response:
                    item_data = await item_response.text()
                    item_soup = BeautifulSoup(item_data, 'lxml')

                    amount_text = item_soup.find('span', id='in_stock').text
                    sale_price_text = item_soup.find('span', id='price').text
                    old_price_text = item_soup.find('span', id='old_price').text

                    amount = int(amount_text.split(' ')[-1])
                    sale_price = int(sale_price_text.split(' ')[0])
                    old_price = int(old_price_text.split(' ')[0])
                    discount = (old_price - sale_price) * amount
                    result.append(discount)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagen:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


soup = get_soup(URL)
get_categories(soup)
get_urls_pages(categories)

asyncio.run(main())
print(sum(result))
