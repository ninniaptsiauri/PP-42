import aiohttp
import asyncio

# rick_morty_url = 'https://rickandmortyapi.com/api/character/1'

# async def fetch_data():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(rick_morty_url) as response:
#             return await response.json()
        
# async def main():
#     response = await fetch_data()
#     print(response)



rick_morty_url = 'https://rickandmortyapi.com/api/character/{id}'

async def fetch_data(session, url):
    try:
        timeout = aiohttp.ClientTimeout(total=10)

        async with session.get(url, timeout=timeout) as response:
            response.raise_for_status()  
            return await response.json()
        
    except aiohttp.ClientResponseError as e:  # 4xx - 5xx
        print(e)

    except aiohttp.ClientConnectionError as e: # couldn't connect to the server
        print(e)

    except aiohttp.ContentTypeError as e: # invalid content type/json
        print(e)

    except asyncio.TimeoutError as e: # timeout 
        print(e)

    except Exception as e:
        print(e)
    

async def main():
    async with aiohttp.ClientSession() as session:
        
        # for i in range(1, 11):
        #     url = rick_morty_url.format(id=i)

        #     response = await fetch_data(session, url)

        #     print(response)

        responses = await asyncio.gather(*[fetch_data(session, rick_morty_url.format(id=i)) for i in range(1, 11)])

        # print(responses)
        for response in responses:
            print(response)

if __name__ == '__main__':
    asyncio.run(main())