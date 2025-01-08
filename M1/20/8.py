import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session, session.get(url) as response:
        return await response.json()


async def main():
    json = await fetch_page('https://api.github.com/users/defunkt')
    print(json)


asyncio.run(main())
