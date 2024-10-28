import asyncio

import requests


async def fetch_data(url):
    print(f"Fetching data from {url}")
    result = await asyncio.to_thread(requests.get, url)
    return result


async def main():
    task1 = asyncio.create_task(fetch_data("https://github.com/"))
    task2 = asyncio.create_task(fetch_data("https://python.org/"))
    # Ждем выполнения задач и получаем результаты
    response1 = await task1
    response2 = await task2
    print(response1.text)
    print(response2.text)


if __name__ == "__main__":
    asyncio.run(main())
