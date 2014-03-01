#!/usr/bin/python
import amicableNumbers 
import unittest

class TestAmicableNumbers(unittest.TestCase):

    def test_divisors(self):
        result = sorted(amicableNumbers.divisors(220))
        self.assertEqual(result, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
    
    def test_amicableNumbers(self):
        result = sum(amicableNumbers.amicableNumbers(10000))
        self.assertEqual(result, 31626)
        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
