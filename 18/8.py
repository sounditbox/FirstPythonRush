import asyncio


def f():  # Функция
    return 42


async def async_f():  # Корутина
    await asyncio.sleep(1)  # Заглушка
    return 42


if __name__ == '__main__':
    result = asyncio.run(async_f())
    print(result)
    # Корутины - это асинхронные функции
