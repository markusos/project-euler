#!/usr/bin/python
import specialPythagoreanTriplet
import unittest

class TestPythagoreanTriplet(unittest.TestCase):

    def test_pythagoreanTriplet(self):
        result = specialPythagoreanTriplet.pythagorean(3,4,5);
        self.assertEqual(result, True)
    
    def test_specialPythagoreanTriplet(self):
        result = specialPythagoreanTriplet.specialPythagoreanTriplet();
        self.assertEqual(result, 31875000)

        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
