import asyncio


class AsyncContextManager:
    async def __aenter__(self):
        print("Enter context")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exit context")


async def main():
    async with AsyncContextManager() as f:
        print(f)
        print("Inside context")


asyncio.run(main())
