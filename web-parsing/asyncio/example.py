import asyncio
import aiohttp
from codetiming import Timer

urls = ["http://google.com",
        "http://yahoo.com",
        "http://apple.com",
        "http://microsoft.com",
        "https://habr.com/",
        "https://stepik.org/",
        "https://docs.python.org/",
        "https://stackoverflow.com/",
        "https://www.reg.ru/"]


async def worker(url, session):
    with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
        async with session.get(url) as resp:
            print(resp.url)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(link, session)) for link in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    with Timer(text=f"Всего затрачено времени на все запросы: {{:.3f}} сек"):
        asyncio.run(main())
