#!/usr/bin/python
import latticePaths
import unittest


class TestLatticePaths(unittest.TestCase):
    def test_latticePaths_2(self):
        result = latticePaths.latticePaths(2)
        self.assertEqual(result, 6)

    def test_latticePaths_20(self):
        result = latticePaths.latticePaths(20)
        self.assertEqual(result, 137846528820)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
