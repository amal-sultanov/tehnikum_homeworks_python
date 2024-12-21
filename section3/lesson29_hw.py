import logging

logging.basicConfig(filename='logs.log', filemode='a',
                    format='%(process)d | %(levelname)s | %(name)s | %(message)s | %(asctime)s',
                    level=logging.ERROR)


def add(number1: int | float, number2: int | float) -> dict:
    return {'addition': number1 + number2}


def subtract(number1: int | float, number2: int | float) -> dict:
    return {'subtraction': number1 - number2}


def multiply(number1: int | float | str, number2: int | float | str) -> dict:
    return {'multiplication': number1 * number2}


try:
    print(add(1, 2))
    print(add(1, 'qwerty'))
except TypeError:
    print('Cannot sum values of different data types')
    logging.error('Cannot sum values of different data types')

try:
    print(subtract(1, 2))
    print(subtract(1, 'qwerty'))
except TypeError:
    print('Cannot make subtraction operation between different data types')
    logging.error('Cannot make subtraction operation between different data types')

try:
    print(multiply(1, 2))
    print(multiply(1, 'qwerty'))
    print(multiply('', ''))
except TypeError:
    print('At least 1 argument should be a number')
    logging.error('At least 1 argument should be a number')
