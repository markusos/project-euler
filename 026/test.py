#!/usr/bin/python
import cycles 
import unittest

class TestCycles (unittest.TestCase):

    def test_fraction(self):
        result = cycles.fractionCycle(2)
        self.assertEqual(result, '')
        result = cycles.fractionCycle(3)
        self.assertEqual(result, '3')
        result = cycles.fractionCycle(4)
        self.assertEqual(result, '')
        result = cycles.fractionCycle(5)
        self.assertEqual(result, '')
        result = cycles.fractionCycle(6)
        self.assertEqual(result, '6')
        result = cycles.fractionCycle(7)
        self.assertEqual(result, '142857')
        result = cycles.fractionCycle(8)
        self.assertEqual(result, '')
        result = cycles.fractionCycle(9)
        self.assertEqual(result, '1')
        result = cycles.fractionCycle(10)
        self.assertEqual(result, '')

    def test_longestCycle(self):
        result = cycles.longestCycle(1000)
        self.assertEqual(result, 983)
        print "Result: {0}".format(result)
        
if __name__ == '__main__':
    unittest.main()
