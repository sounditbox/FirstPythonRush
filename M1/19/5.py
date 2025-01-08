import asyncio


async def greet():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Again!")


loop = asyncio.get_event_loop()
loop.run_until_complete(greet())
loop.close()
