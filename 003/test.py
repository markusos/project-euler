#!/usr/bin/python
import factor
import unittest

class TestFactor(unittest.TestCase):

    def test_factor_13195(self):
        self.number = 13195
        result = factor.factors(self.number);
        self.assertEqual(sorted(result), [5, 7, 13, 29])
    
    def test_factor_600851475143(self):
        self.number = 600851475143
        result = factor.factors(self.number);
        self.assertEqual(result, [6857L, 1471L, 839L, 71L])

        print "Result: {0}".format(result)
        print "Largest factor: {0}".format(sorted((result), reverse=True)[0])

if __name__ == '__main__':
    unittest.main()
