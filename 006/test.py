#!/usr/bin/python
import sumSquareDiff
import unittest

class TestSumSquareDiff(unittest.TestCase):

    def test_sumSquareDiff_10(self):
        self.number = 10
        result = sumSquareDiff.sumSquareDiff(self.number);
        self.assertEqual(result, 2640)

    def test_sumSquareDiff_100(self):
        self.number = 100
        result = sumSquareDiff.sumSquareDiff(self.number);
        self.assertEqual(result, 25164150)

        print "Result: {0}".format(result)

if __name__ == '__main__':
    unittest.main()
