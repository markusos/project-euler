#!/usr/bin/python
import multiplesSum
import unittest


class TestMultiples(unittest.TestCase):
    def test_3_and_5_below_10(self):
        self.multiples = [3, 5]
        self.below = 10
        result = multiplesSum.multiplesSum(self.multiples, self.below)
        self.assertEqual(result, 23)

    def test_3_and_5_below_1000(self):
        self.multiples = [3, 5]
        self.below = 1000
        result = multiplesSum.multiplesSum(self.multiples, self.below)
        self.assertEqual(result, 233168)

        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
