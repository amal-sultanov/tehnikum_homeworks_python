import asyncio


# def show_products(products):
#     for product in products:
#         print(f'{product}')
#
#
# products = ['qwer', 'qweqrt', 'q3rwtre']
# thread1 = Thread(target=show_products, args=(products,))
# thread1.run()
# print('hello')


# def send_messages(users):
#     for user in users:
#         print(user)
#
#
# user_list = ['Jordan', 'Pasha', 'Mikle']
# thread1 = Thread(target=send_messages, args=(user_list,))
# thread1.start()
# print('Hello potok world')


# def check_queue(clients):
#     for client in clients:
#         yield client
#
#
# all_clients = ['Pasha', 'Jordan', 'Vika']
# hospital = list(check_queue(all_clients))
#
# for i in range(len(list(hospital))):
#     print(next(hospital))


# def week_days(days):
#     for day in days:
#         yield day
#
#
# days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
# d = week_days(days)


# async def send_message(users):
#     for i in users:
#         print(i)
#
#
# user_list = ['Jordan', 'Pasha', 'Michael']
#
#
# async def main():
#     await asyncio.create_task(send_message(user_list))


async def task1():
    # print('Task 1')
    await asyncio.sleep(5)


async def task2():
    # print('Task 2')
    await asyncio.sleep(5)


async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    task_group = await asyncio.gather(t1, t2)
    print(task_group)

    await asyncio.gather(t1, t2)


asyncio.run(main())
