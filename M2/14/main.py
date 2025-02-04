import asyncio


async def coro():
    return 42


async def main():
    res = coro()
    print(res)


asyncio.run(main())
