#!/usr/bin/python
import multiples
import unittest

class TestMultiples(unittest.TestCase):

    def test_smallest_multiple_10(self):
        result = multiples.multiples(10);
        self.assertEqual(result, 2520)

    def test_smallest_multiple_20(self):
        result = multiples.multiples(20);
        self.assertEqual(result, 232792560)
        print("Result: {0}".format(result))
        
if __name__ == '__main__':
    unittest.main()
