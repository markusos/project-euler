#!/usr/bin/python
import pandigital
import unittest


class TestPandigitalProduct(unittest.TestCase):

    def test_is_pandigital_product_true(self):
        result = pandigital.is_9_pandigit("391867254")
        self.assertEqual(result, True)
        result = pandigital.is_9_pandigit("123456789")
        self.assertEqual(result, True)

    def test_is_pandigital_product_false(self):
        result = pandigital.is_9_pandigit("123456799")
        self.assertEqual(result, False)
        result = pandigital.is_9_pandigit("1234567891")
        self.assertEqual(result, False)
        result = pandigital.is_9_pandigit("123456780")
        self.assertEqual(result, False)


    def test_pandigital_product(self):
        result = pandigital.count_9_pandigit()
        print("Result: {0}".format(result))
        self.assertEqual(result, 45228)



if __name__ == '__main__':
    unittest.main()