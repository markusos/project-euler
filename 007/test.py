#!/usr/bin/python
import euler
import unittest

class TestEuler(unittest.TestCase):

    def test_euler_6(self):
        self.number = 6
        result = euler.euler(self.number)[self.number-1];
        self.assertEqual(result, 13)
        
    def test_euler_10001(self):
        self.number = 10001
        result = euler.euler(self.number)[self.number-1];
        self.assertEqual(result, 104743)

        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
