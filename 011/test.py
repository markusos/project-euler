#!/usr/bin/python
import grid
import unittest

class TestGrid(unittest.TestCase):

    def test_grid(self):
        self.grid = grid.readGrid();
        result = grid.checkGrid(self.grid);
        self.assertEqual(result, 70600674)

        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
