import asyncio

async def cube(n):
    await asyncio.sleep(4)
    return n*n*n

async def main():
    result=await asyncio.gather(
        cube(5),
        cube(4),
        cube(6)
    )
    print(result)
asyncio.run(main())
    