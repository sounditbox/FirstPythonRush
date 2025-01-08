import asyncio
from random import randint


async def download(code):
    wait_time = randint(1, 3)
    print(f'downloading {code} will take {wait_time} second(s)')
    await asyncio.sleep(wait_time)  # I/O, context will switch to main function
    print(f'downloaded {code}')


sem = asyncio.Semaphore(3)
lock = asyncio.Lock()
barrier = asyncio.Barrier(4)
queue = asyncio.Queue()


async def safe_download(i):
    async with sem:
        await download(i)


async def main():
    tasks = [asyncio.create_task(safe_download(i)) for i in range(9)]
    await asyncio.gather(*tasks)  # await moment all downloads done


if __name__ == '__main__':
    asyncio.run(main())
