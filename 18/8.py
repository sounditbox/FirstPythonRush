import asyncio


def f():  # Функция
    return 42


async def async_f():  # Корутина
    await asyncio.sleep(1)
    return 42


async def main():
    print(f())
    print(await async_f())


if __name__ == '__main__':
    main()
    # Корутины - это асинхронные функции
