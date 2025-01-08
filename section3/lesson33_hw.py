import unittest


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_numbers(self):
        return self.x + self.y

    def subtract_numbers(self):
        return self.x - self.y

    def divide_numbers(self):
        return self.x / self.y

    def multiply_numbers(self):
        return self.x * self.y


class TestCalculator(unittest.TestCase):
    def test_green_add_numbers(self):
        return self.assertEqual(Calculator(4, 3).add_numbers(), 7,
                                'Answer is incorrect')

    def test_red_add_numbers(self):
        return self.assertEqual(Calculator(1, 2).add_numbers(), 5,
                                'Answer is incorrect')

    def test_green_subtract_numbers(self):
        return self.assertEqual(Calculator(10, 5).subtract_numbers(), 5,
                                'Answer is incorrect')

    def test_red_subtract_numbers(self):
        return self.assertEqual(Calculator(3, 5).subtract_numbers(), 0,
                                'Answer is incorrect')

    def test_green_divide_numbers(self):
        return self.assertEqual(Calculator(8, 4).divide_numbers(), 2,
                                'Answer is incorrect')

    def test_red_divide_numbers(self):
        return self.assertEqual(Calculator(20, 5).divide_numbers(), 1,
                                'Answer is incorrect')

    def test_green_multiply_numbers(self):
        return self.assertEqual(Calculator(9, 5).multiply_numbers(), 45,
                                'Answer is incorrect')

    def test_red_multiply_numbers(self):
        return self.assertEqual(Calculator(3, 5).multiply_numbers(), 65,
                                'Answer is incorrect')


if __name__ == '__main__':
    unittest.main()
