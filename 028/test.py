#!/usr/bin/python
import spiral
import unittest


class TestSpiral(unittest.TestCase):
    def test_spiral_5(self):
        result = spiral.diagonalSum(spiral.spiral(5))
        self.assertEqual(result, 101)

    def test_spiral_1001(self):
        result = spiral.diagonalSum(spiral.spiral(1001))
        self.assertEqual(result, 669171001)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
