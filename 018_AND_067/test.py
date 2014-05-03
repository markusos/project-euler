#!/usr/bin/python
import maxPath 
import unittest

class TestMaxPath (unittest.TestCase):

    def test_maxPathSum_0(self):
        result = maxPath.maxPath("triangle_small.txt")
        self.assertEqual(result, 23)
    
    def test_maxPathSum_1(self):
        result = maxPath.maxPath("triangle.txt")
        self.assertEqual(result, 1074)
        print("Result: {0}".format(result))

    def test_maxPathSum_2(self):
        result = maxPath.maxPath("triangle_big.txt")
        self.assertEqual(result, 7273)
        print("Result: {0}".format(result))

    def test_maxPathSum_3(self):
        result = maxPath.maxPath("triangle2.txt")
        self.assertEqual(result, 732506)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
