import asyncio

import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry

links = ['https://parsinger.ru/html/watch/1/1_1.html',
         'https://parsinger.ru/html/watch/1/1_2.html',
         'https://parsinger.ru/html/watch/1/1_3.html',
         'https://parsinger.ru/html/watch/8/1_3.html',
         'https://parsinger.ru/html/watch/8/2_3.html']


async def get_data(retry_client, link):
    async with retry_client.get(link) as response:
        print(f'{link}: {response.status}')


async def main():
    async with aiohttp.ClientSession() as client_session:
        retry_options = ExponentialRetry(attempts=4, statuses={404,403})
        async with RetryClient(
            raise_for_status=False,
            retry_options=retry_options,
            client_session=client_session,
        ) as retry_client:
            tasks = [get_data(retry_client, link) for link in links]
            await asyncio.gather(*tasks)


if __name__== '__main__':
    asyncio.run(main())
