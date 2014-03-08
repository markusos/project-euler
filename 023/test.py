#!/usr/bin/python
import abundantNumbers 
import unittest

class TestAbundantNumbers (unittest.TestCase):
    
    def test_abundantNumbers(self):
        result = len(abundantNumbers.abundantNumbers(100))
        self.assertEqual(result, 21)
        result = abundantNumbers.abundantNumbers(40)
        self.assertEqual(sorted(result), [12, 18, 20, 24, 30, 36])  

    def test_nonAbundentNumberSum(self):
        result = abundantNumbers.nonAbundentNumberSum()
        self.assertEqual(result, 4179871)
        print("Result: {0}".format(result))
        
if __name__ == '__main__':
    unittest.main()
