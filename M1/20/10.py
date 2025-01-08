import asyncio

import aiohttp
import grequests


class AsyncURLFetchIterator:
    def __init__(self, urls: list[str]):
        self.urls = urls
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= len(self.urls):
            raise StopAsyncIteration
        async with aiohttp.ClientSession() as session, session.get(self.urls[self.current]) as response:
            res = await response.json()

        self.current += 1
        return res


urls = [
    'https://api.github.com/users/defunkt',
    'https://api.github.com/users/defunkt',
    'https://api.github.com/users/defunkt',
    'https://api.github.com/users/defunkt',
    'https://api.github.com/users/defunkt',
]


async def main():
    async for data in AsyncURLFetchIterator(urls):
        print(data)


asyncio.run(main())
