#!/usr/bin/python
import factorial
import unittest


class TestFactorialunittest(unittest.TestCase):
    def test_factorial(self):
        result = factorial.factorial(10)
        self.assertEqual(result, 3628800)

    def test_factorialSum_10(self):
        result = factorial.factorialSum(10)
        self.assertEqual(result, 27)

    def test_factorialSum_100(self):
        result = factorial.factorialSum(100)
        self.assertEqual(result, 648)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
