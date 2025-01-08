import unittest


# TODO qweqwe

# def check_positive_numbers(x, y):
#     assert x > 0 and y > 0, 'Numbers are negative'
#     return x, y
#
#
# check_positive_numbers(20, 30)
# check_positive_numbers(-2, -5)
# check_positive_numbers(50, 20)
#
#
# def check_positive_numbers(x, y):
#     assert x > 0 or y < 0, 'Numbers are negative'
#     return x, y
#
#
# check_positive_numbers(20, 30)
# check_positive_numbers(-2, -5)
# check_positive_numbers(50, 20)


# def product(a, b):
#     return a * b
#
#
# def compare_numbers(a, b):
#     if a > b:
#         return True
#     elif a < b:
#         return False
#
#
# def test1():
#     """
#     >>> product(1, 2)
#     2
#     >>> product(1, 3)
#     1
#     >>> compare_numbers(2, 0)
#     True
#     >>> compare_numbers(10, 5)
#     False
#     """


def product(a, b):
    return a * b


def compare_numbers(a, b):
    if a > b:
        return True
    elif a < b:
        return False


class TestOne(unittest.TestCase):
    def test_green_product(self):
        return self.assertEqual(product(2, 6), 12, 'Cannot multiply')

    def test_green_compare(self):
        return self.assertEqual(compare_numbers(6, 2), True,
                                'First number is less than the second')

    def test_red_product(self):
        return self.assertEqual(product(3, 4), 18, 'Wrong answer')


if __name__ == '__main__':
    unittest.main()
