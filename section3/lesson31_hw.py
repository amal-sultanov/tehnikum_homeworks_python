import asyncio
from threading import Thread


def display_red():
    print('red')


def display_yellow():
    print('yellow')


def display_green():
    print('green')


# synchronous
display_red()
display_yellow()
display_green()

# multithreading
thread1 = Thread(target=display_red)
thread2 = Thread(target=display_yellow)
thread3 = Thread(target=display_green)

thread1.start()
thread2.start()
thread3.start()


# asynchronous
async def display_red():
    print('red')


async def display_yellow():
    print('yellow')


async def display_green():
    print('green')


async def main():
    t1 = asyncio.create_task(display_red())
    t2 = asyncio.create_task(display_yellow())
    t3 = asyncio.create_task(display_green())

    await t1, t2, t3


asyncio.run(main())
