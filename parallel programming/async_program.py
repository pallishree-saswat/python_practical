# Asynchronous Programming python
# send much request parallaly and get response
# we wont wait for the first response


# In python there are 4 ways to acheive asynchronous program

# multiprocess
import asyncio
from multiprocessing import Process


def showSquare(num):
    print(num ** 2)

# multi Threading

# Couroutines

# AsyncIO

# retrun a couroutine


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("World")

if __name__ == '__main__':
    print(type(main()))
    asyncio.run(main())
