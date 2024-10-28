import asyncio
import time

import requests


async def fetch_data(url):
    print(f"Fetching data from {url}")
    result = await asyncio.to_thread(requests.get, url)
    return result


async def main():
    start = time.time()
    tasks = asyncio.gather(*[fetch_data(url) for url in ["https://github.com/", "https://python.org/"] * 10])
    results = await tasks
    end = time.time()
    print(results)
    print(end - start)


if __name__ == "__main__":
    asyncio.run(main())
