#!/usr/bin/python
import distinctPowers
import unittest


class TestDistinctPowers(unittest.TestCase):

    def test_distinctPowers_small(self):
        result = distinctPowers.distinctPowers(5, 5)
        self.assertEqual(result, 15)
        print("Result: {0}".format(result))

    def test_distinctPowers(self):
        result = distinctPowers.distinctPowers(100, 100)
        self.assertEqual(result, 9183)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()