import asyncio

async def call(i):
    await asyncio.sleep(1)
    return i*2

async def main():
    result= await asyncio.gather(         #This is where concurrency happens
        *(call(i) for i in range(10))

    )
    print(result)

asyncio.run(main())
