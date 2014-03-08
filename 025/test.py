#!/usr/bin/python
import fib 
import unittest

class TestFib (unittest.TestCase):

    def test_fib(self):
        fib.init()
        result = fib.nextFib()
        self.assertEqual(result, 2)
        result = fib.nextFib()
        self.assertEqual(result, 3)
        result = fib.nextFib()
        self.assertEqual(result, 5)
        result = fib.nextFib()
        self.assertEqual(result, 8)
        result = fib.nextFib()
        self.assertEqual(result, 13)
        result = fib.nextFib()
        self.assertEqual(result, 21)

    def test_fibOfLength_3(self):
        result = fib.fibOfLength(3)
        self.assertEqual(result, 12)
      
    def test_fibOfLength_1000(self):
        result = fib.fibOfLength(1000)
        self.assertEqual(result, 4782)
        print("Result: {0}".format(result))
        
if __name__ == '__main__':
    unittest.main()
