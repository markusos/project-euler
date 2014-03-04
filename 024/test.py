#!/usr/bin/python
import permutations 
import unittest

class TestPermutations (unittest.TestCase):

    def test_small_permutations(self):
        self.data = ["0","1","2"]
        self.index = 6-1
        result = permutations.permutation(self.index, self.data)
        self.assertEqual(result, "210")
    
    def test_permutations(self):
        self.data = ["0","1","2","3","4","5","6","7","8","9"]
        self.index = 1000000-1
        result = permutations.permutation(self.index, self.data)
        self.assertEqual(result, "2783915460")
        print "Result: {0}".format(result)
        
if __name__ == '__main__':
    unittest.main()
