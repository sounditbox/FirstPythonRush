import asyncio


async def main():
    task = asyncio.create_task(asyncio.sleep(1))
    await asyncio.sleep(1.1)
    print(task.done())  # Output: True


asyncio.run(main())
