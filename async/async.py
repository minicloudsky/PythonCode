import asyncio
import aiohttp
import time


async def request(sleep_time):
    async with aiohttp.ClientSession() as client:
        resp = await client.get('https://api.bilibili.com/x/web-interface/search/default')
        resp_json = await resp.json()
        print(resp_json)


async def main():
    start = time.perf_counter()
    await request(1)
    a = 1 + 1
    b = 2 + 2
    print('能不能在第一个请求等待的过程中运行到这里？')
    await request(2)
    print('能不能在第二个请求等待的过程中运行到这里？')
    await request(3)

    end = time.perf_counter()
    print(f'总计耗时：{end - start}')


if __name__ == '__main__':
    asyncio.run(main())
