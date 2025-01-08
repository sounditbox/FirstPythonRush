import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return what


async def main():
    tasks = asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )
    results = await tasks
    print(results)


asyncio.run(main())
