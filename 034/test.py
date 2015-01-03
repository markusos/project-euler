#!/usr/bin/python
import digitFactorials
import unittest


class TestDigitCancellingFractions(unittest.TestCase):
    def test_is_digit_factorial(self):

        result = digitFactorials.is_digit_factorial(145)
        self.assertEqual(result, True)

        result = digitFactorials.is_digit_factorial(1)
        self.assertEqual(result, False)

        result = digitFactorials.is_digit_factorial(2)
        self.assertEqual(result, False)

    def test_find_digit_factorials(self):
        result = digitFactorials.find_digit_factorial(99999)
        result = sum(result);

        self.assertEqual(result, 40730)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()