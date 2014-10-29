#!/usr/bin/python
import digitPowers
import unittest


class TestDigitPowers(unittest.TestCase):
    def test_digitPowers_small(self):
        result = digitPowers.digitPowersSum(4)
        self.assertEqual(result, 19316)
        print("Result: {0}".format(result))

    def test_digitPowers(self):
        result = digitPowers.digitPowersSum(5)
        self.assertEqual(result, 443839)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()