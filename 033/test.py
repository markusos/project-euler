#!/usr/bin/python
import digitCancellingFractions
import unittest


class TestDigitCancellingFractions(unittest.TestCase):
    def test_digit_cancelling_fractions(self):
        result = digitCancellingFractions.digit_cancelling_fractions()
        self.assertEqual(result, 100)
        print("Result: {0}".format(result))

    def test_naive_cancelation(self):
        result = digitCancellingFractions.naive_cancellation(49, 98)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()