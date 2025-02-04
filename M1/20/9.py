import asyncio


class AsyncIterator:
    def __init__(self, start, end):
        self.current = start - 1
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(1)  # Имитация асинхронной задержки

        self.current += 1
        return self.current


async def main():
    async for number in AsyncIterator(1, 5):
        print(number)


asyncio.run(main())
