import asyncio
import time

import requests


async def fetch_data(url):
    print(f"Fetching data from {url}")
    result = await asyncio.to_thread(requests.get, url)
    return result


async def main():
    urls = ["https://github.com/", "https://python.org/"] * 50
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(fetch_data(url)))
    results = []
    start = time.time()
    for task in tasks:
        result = await task
        results.append(result)
    end = time.time()
    print(results)
    print(end - start)

if __name__ == "__main__":
    asyncio.run(main())

