import asyncio
import aiohttp

BASE_URL = 'https://jsonplaceholder.typicode.com/todos/{id}'

async def fetch_data(session, url):
    response = await session.get(url)
    return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, BASE_URL.format(id=id)) for id in range(1, 11)]
        result = await asyncio.gather(*tasks)
        for res in result:
            print(res)


asyncio.run(main())