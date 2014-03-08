#!/usr/bin/python
import powerDigitSum 
import unittest

class TestPowerDigitSum(unittest.TestCase):

    def test_powerDigitSum_15(self):
        result = powerDigitSum.powerDigitSum(15)
        self.assertEqual(result, 26)

    def test_powerDigitSum_1000(self):
        result = powerDigitSum.powerDigitSum(1000)
        self.assertEqual(result, 1366)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
