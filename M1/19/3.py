import asyncio


async def coroutine(s):
    await asyncio.sleep(s)
    return 42


async def main():
    coro = coroutine(2)
    print('Hello')
    print('This is code before awaiting')
    await coro
    print('And this is after')


asyncio.run(main())
