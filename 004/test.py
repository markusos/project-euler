#!/usr/bin/python
import palindrom
import unittest

class TestPalindrom(unittest.TestCase):

    def test_palindrom_product_100(self):
        self.below = 100
        result = palindrom.largestPalindromFromProduct(self.below);
        self.assertEqual(result, 9009)
    
    def test_palindrom_product_1000(self):
        self.below = 1000
        result = palindrom.largestPalindromFromProduct(self.below);
        self.assertEqual(result, 906609)

        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
