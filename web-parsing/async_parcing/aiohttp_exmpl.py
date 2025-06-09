import aiohttp
import asyncio

url = 'https://parsinger.ru/html/index1_page_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/105.0.0.0 Safari/537.36'}
data = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103',
        'format': 'xml',
        'platformId': 1}

async def main():
    async with aiohttp.ClientSession(trust_env=True) as s:
        async with s.get(url=url,
                         headers=headers,
                         timeout=1,
                         params=data) as response:
            html = await response.text()
            print(html)


asyncio.run(main())
