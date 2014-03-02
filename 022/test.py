#!/usr/bin/python
import namesScores 
import unittest

class TestNamesScores (unittest.TestCase):

    def test_stringScore(self):
        result = namesScores.stringScore("COLIN")
        self.assertEqual(result, 53) 
    
    def test_namesScores(self):
        result = namesScores.namesScores()
        self.assertEqual(result, 871198282)
        print "Result: {0}".format(result)
        
if __name__ == '__main__':
    unittest.main()
