#!/usr/bin/python
import circularPrimes
import unittest


class TestCircularPrimes(unittest.TestCase):
    def test_rotations(self):
        result = circularPrimes.rotations(123)
        self.assertEqual(result, [123, 231, 312])

    def test_primes(self):
        result = circularPrimes.primes(10)
        self.assertEqual(result, [2, 3, 5, 7])

    def test_find_circular_primes(self):
        result = circularPrimes.find_circular_primes(100)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])
        self.assertEqual(len(result), 13)

        result = circularPrimes.find_circular_primes(1000000)
        self.assertEqual(len(result), 55)
        print("Result: {0}".format(len(result)))

if __name__ == '__main__':
    unittest.main()
