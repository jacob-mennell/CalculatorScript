import unittest
from calculator import calculator


class CalculatorOutputTest(unittest.TestCase):

    def test_calculator(self):
        """ Test case to check function is outputting as expected """
        self.assertEqual(calculator(), 46, msg='Function output not as expected')


if __name__ == '__main__':
    unittest.main()
