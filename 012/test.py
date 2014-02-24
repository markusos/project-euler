#!/usr/bin/python
import triangular 
import unittest

class TestTriangular (unittest.TestCase):

    def test_triangular (self):
        result = triangular.triangularNumber();
        self.assertEqual(result, 76576500)
        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
