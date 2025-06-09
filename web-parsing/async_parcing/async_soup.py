import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup


# 1. Soup 1.
async def main():
    url = 'https://parsinger.ru/html/index1_page_1.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, timeout=1) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            name = soup.find_all('a', class_='name_item')
            price = soup.find_all('p', class_='price')
            for n, p in zip(name, price):
                print(n.text, p.text)


# asyncio.run(main())


# 2. Soup 2.
category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html'
         for cat, i in zip(category, range(1, len(category) + 1))
              for x in range(1, 33)]


async def run_tasks(url, session):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        price = soup.find('span', id='price').text
        name = soup.find('p', id='p_header').text
        print(resp.url, price, name)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(link, session) for link in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)
