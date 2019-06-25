#!/usr/bin/python
import integerRightTriangles
import unittest


class IntegerRightTriangles(unittest.TestCase):
    def test_is_pythagorean_triple(self):
        result = integerRightTriangles.is_pythagorean_triple(20, 48, 52)
        self.assertEqual(result, True)
        result = integerRightTriangles.is_pythagorean_triple(24, 45, 51)
        self.assertEqual(result, True)
        result = integerRightTriangles.is_pythagorean_triple(30, 40, 50)
        self.assertEqual(result, True)
        result = integerRightTriangles.is_pythagorean_triple(12, 13, 14)
        self.assertEqual(result, False)

    def test_pythagorean_triples(self):
        result = integerRightTriangles.pythagorean_triples(120)
        self.assertEqual(result[120], [[20, 48, 52], [24, 45, 51], [30, 40, 50]])

    def test_max_pythagorean_triples(self):
        result = integerRightTriangles.max_pythagorean_triples(100)
        self.assertEqual(result, 60)
        result = integerRightTriangles.max_pythagorean_triples(1000)
        self.assertEqual(result, 840)

if __name__ == '__main__':
    unittest.main()
