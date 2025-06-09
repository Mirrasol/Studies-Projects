import asyncio

import aiohttp

import requests
from bs4 import BeautifulSoup

categories = []
pagen = []
domain = 'https://parsinger.ru/html/'


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')


def get_urls_categories(soup):
    links = soup.find('div', class_='nav_menu').find_all('a')

    for cat in links:
        categories.append(domain + cat['href'])


def get_urls_pages(categories):
    for cat in categories:
        response = requests.get(cat)
        soup = BeautifulSoup(response.text, 'lxml')
        for page in soup.find('div', class_='pagen').find_all('a'):
            pagen.append(domain + page['href'])


async def get_data(session, link):
    async with session.get(link) as response:
        resp = await response.text()
        soup = BeautifulSoup(resp, 'lxml')
        item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
        for x in item_card:
            url2 = domain + x
            async with session.get(url2) as response2:
                resp2 = await response2.text()
                soup2 = BeautifulSoup(resp2, 'lxml')
                article = soup2.find('p', class_='article').text
                name = soup2.find('p', id='p_header').text
                price = soup2.find('span', id='price').text
                print(url2, price, article, name)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagen:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(categories)

asyncio.run(main())
