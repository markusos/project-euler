#!/usr/bin/python
import truncatablePrimes
import unittest


class TestTruncatablePrimes(unittest.TestCase):
    def test_is_truncatable_prime(self):
        primes, is_prime = truncatablePrimes.eratosthenes(5000)
        result = truncatablePrimes.is_truncatable_prime(3797, is_prime)
        self.assertEqual(result, True)
        result = truncatablePrimes.is_truncatable_prime(797, is_prime)
        self.assertEqual(result, True)
        result = truncatablePrimes.is_truncatable_prime(379, is_prime)
        self.assertEqual(result, False)
        result = truncatablePrimes.is_truncatable_prime(11, is_prime)
        self.assertEqual(result, False)

    def test_truncatable_primes_sum(self):
        result = truncatablePrimes.truncatable_primes_sum(1000000)
        self.assertEqual(result, 748317)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
