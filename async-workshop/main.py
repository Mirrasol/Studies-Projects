import asyncio
# import time


async def send_request(id):
    print('Start sending here.')
    await asyncio.sleep(1)
    print('Has been sent.')


async def calculate(id):
    print('Calculated successfully.')


async def fetch_response(id):
    print('Start fetching.')
    await asyncio.sleep(2)
    print('Has been fetched.')


async def process(id):
    await send_request(id)
    await calculate(id)
    await fetch_response(id)
    print('\n')


async def process_all():
    await asyncio.gather(send_request(1), send_request(2))


# if __name__ == '__main__':
#     asyncio.run(process_all())

async def return_five():
    await asyncio.sleep(0.2)
    return 5


async def main():
    number = await return_five()
    return number

number = asyncio.run(main())
print(number)
