#!/usr/bin/python
import fibonacci
import unittest

class TestFibonacci(unittest.TestCase):

    def test_even_fib_below_40(self):
        self.below = 40
        fibonacci.init()
        result = fibonacci.evenFibSum(self.below);
        self.assertEqual(result, 44)
    
    def test_even_fib_below_4M(self):
        self.below = 4000000
        fibonacci.init()
        result = fibonacci.evenFibSum(self.below);
        self.assertEqual(result, 4613732)
        
        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
