#!/usr/bin/python
import doubleBasePalindromes
import unittest


class TestDoubleBasePalindromes(unittest.TestCase):
    def test_is_palindrome(self):
        result = doubleBasePalindromes.is_palindrome(123)
        self.assertEqual(result, False)
        result = doubleBasePalindromes.is_palindrome(585)
        self.assertEqual(result, True)
        result = doubleBasePalindromes.is_palindrome(1001001001)
        self.assertEqual(result, True)

    def test_is_double_based_palindrome(self):
        result = doubleBasePalindromes.is_double_based_palindrome(585)
        self.assertEqual(result, True)
        result = doubleBasePalindromes.is_double_based_palindrome(101)
        self.assertEqual(result, False)

    def test_sum_double_based_palindromes(self):
        result = doubleBasePalindromes.sum_double_based_palindromes(1000)
        self.assertEqual(result, 1772)
        result = doubleBasePalindromes.sum_double_based_palindromes(1000000)
        self.assertEqual(result, 872187)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
