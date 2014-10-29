#!/usr/bin/python
import quadraticPrimes
import unittest


class TestQuadraticPrimes(unittest.TestCase):
    def test_count_quadratic_primes_1(self):
        result = quadraticPrimes.count_consecutive_primes(1, 41)
        self.assertEqual(result, 40)

    def test_count_quadratic_primes_2(self):
        result = quadraticPrimes.count_consecutive_primes(-79, 1601)
        self.assertEqual(result, 80)

    def test_quadratic_primes(self):
        result = quadraticPrimes.find_optimal_quadratic_primes(1000)
        self.assertEqual(result[0] * result[1], -59231)
        print("Result: {0}".format(result[0] * result[1]))


if __name__ == '__main__':
    unittest.main()
