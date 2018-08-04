#!/usr/bin/python
import pandigitalMultiples
import unittest


class TestPandigitalMultiples(unittest.TestCase):
    def test_is_pandigital(self):
        result = pandigitalMultiples.is_pandigital(192384576)
        self.assertEqual(result, True)
        result = pandigitalMultiples.is_pandigital(918273645)
        self.assertEqual(result, True)
        result = pandigitalMultiples.is_pandigital(192384579)
        self.assertEqual(result, False)

    def test_is_pandigital_base(self):
        result = pandigitalMultiples.is_pandigital_base(192)
        self.assertEqual(result, 192384576)
        result = pandigitalMultiples.is_pandigital_base(9)
        self.assertEqual(result, 918273645)
        result = pandigitalMultiples.is_pandigital_base(23)
        self.assertEqual(result, False)

    def test_max_pandigital(self):
        result = pandigitalMultiples.max_pandigital()
        self.assertEqual(result, 932718654)

if __name__ == '__main__':
    unittest.main()
