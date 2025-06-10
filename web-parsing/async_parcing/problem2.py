import asyncio

import aiohttp
import lxml  # noqa F401

import requests
from bs4 import BeautifulSoup

BASE = 'https://parsinger.ru/asyncio/create_soup/1/'
URL = 'https://parsinger.ru/asyncio/create_soup/1/index.html'

links = []
result = []


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_links(soup):
    for link in soup.find('div', class_='item_card').find_all('a'):
        links.append(BASE + link['href'])


async def get_data(session, link):
    async with session.get(url=link) as response:
        if response.ok:
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            num = int(soup.find('p', class_='text').text)
            result.append(num)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in links:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


soup = get_soup(URL)
get_links(soup)

asyncio.run(main())
print(sum(result))
