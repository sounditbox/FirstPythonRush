import asyncio


async def coroutine():
    print('hello')
    await asyncio.sleep(2)
    print('world')


asyncio.run(coroutine())
