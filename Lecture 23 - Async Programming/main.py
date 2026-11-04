import asyncio
import time


async def fetch_data():
    await asyncio.sleep(2)

    int("Hello")
    print("Hello")

async def main():
    start = time.time()

    # await fetch_data()
    # await fetch_data()
    # await fetch_data()

    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    task3 = asyncio.create_task(fetch_data())

    print("Tasks created, waiting for them to complete...")

    # await task1
    # await task2
    # await task3

    result = asyncio.gather(task1, task2, task3, return_exceptions=True)

    res = await result
    print(res)

    end = time.time()
    print(f"Total time taken: {end - start} seconds")

if __name__ == "__main__":
    asyncio.run(main())