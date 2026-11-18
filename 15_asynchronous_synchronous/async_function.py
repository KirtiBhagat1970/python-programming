import asyncio

async def func():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to the world of python")
    await asyncio.sleep(2)
    print("asynchronous function in python")
    
    
asyncio.run(func())