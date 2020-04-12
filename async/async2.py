import aiohttp
import asyncio
import time


async def request(sleep_time):
    async with aiohttp.ClientSession() as client:
        resp = await client.get(f'https://api.bilibili.com/x/web-interface/search/default')
        resp_json = await resp.json()
        print(resp_json)


async def main():
    start = time.perf_counter()
    tasks_list = [
        asyncio.create_task(request(1)),
        asyncio.create_task(request(2)),
        asyncio.create_task(request(3)),
    ]
    await asyncio.gather(*tasks_list)
    end = time.perf_counter()
    print(f'总计耗时：{end - start}')


asyncio.run(main())
