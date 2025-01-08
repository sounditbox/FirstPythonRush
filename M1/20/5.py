import asyncio


async def set_future_exception(fut, delay):
    await asyncio.sleep(delay)
    fut.set_exception(ValueError("An error occurred"))


asyncio.Future


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await asyncio.create_task(set_future_exception(fut, 2))
    try:
        result = await fut
    except ValueError as e:
        print(f"Caught an exception: {e}")


asyncio.run(main())
