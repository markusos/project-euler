#!/usr/bin/python
import multiples
import unittest

class TestMultiples(unittest.TestCase):

    def test_smallest_multiple_10(self):
        self.number = 10
        result = multiples.multiples(self.number);
        self.assertEqual(result, 2520)

    def test_smallest_multiple_20(self):
        self.number = 20
        result = multiples.multiples(self.number);
        self.assertEqual(result, 232792560)

        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
