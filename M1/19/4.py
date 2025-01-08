import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return 42


async def main():
    task1 = asyncio.create_task(say_after(3, 'Первая'))
    task2 = asyncio.create_task(say_after(1, 'Вторая'))
    task3 = asyncio.create_task(say_after(2, 'Третья'))
    await task2
    await task3
    await task1
    print('Все корутины выполнились')


asyncio.run(main())
