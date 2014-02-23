#!/usr/bin/python
import eratosthenes
import unittest

class TestEratosthenes(unittest.TestCase):

    def test_eratosthenes_10(self):
        result = eratosthenes.primeSum(10);
        self.assertEqual(result, 17)
    
    def test_eratosthenes_2M(self):
        result = eratosthenes.primeSum(2000000);
        self.assertEqual(result, 142913828922)

        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
