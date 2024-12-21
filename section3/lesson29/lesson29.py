import logging

# DEBUG - 0
# INFO - 10
# WARNING - 20
# ERROR - 30
# CRITICAL - 40
# separate file foe each level

logging.basicConfig(filename='logs/logs.log', filemode='a',
                    format='%(asctime)s | %(process)d | %(name)s | %(levelname)s | %(message)s',
                    level=logging.INFO)
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

# def extend_arr(a: list, b: list) -> list:
#     return a.extend(b)

# number = input("Enter a number: ")
# numbers = ()
#
# try:
#     print(int(number) * 5)
# except ValueError:
#     print('Only numbers')
#
# try:
#     numbers.append(number)
# except AttributeError:
#     print('Cannot add values to tuple')
#
# m = 34
# spam = 'qwerty'
#
# try:
#     m + spam
# except TypeError:
#     print('Error!')
#
# try:
#     spammer = (10, 11, 12)
#     spammer.append(13)
# except AttributeError:
#     print('Cannot add values to tuple')
