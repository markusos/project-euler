#!/usr/bin/python
import bigInt
import unittest


class TestBigInt(unittest.TestCase):
    def test_add(self):
        a = bigInt.bigInt([1, 0])
        b = bigInt.bigInt([1, 1, 0])
        a.add(b)
        result = a.getNumberString()
        self.assertEqual(result, "120")

    def test_bigInt(self):
        result = str(bigInt.sumNumbers())[:10]
        self.assertEqual(result, "5537376230")
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
