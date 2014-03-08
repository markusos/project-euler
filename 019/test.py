#!/usr/bin/python
import sundays 
import unittest

class TestSundays(unittest.TestCase):

    def test_day_today(self):
        result = sundays.weekday(2014, 2, 28)
        self.assertEqual(result, 5)

    def test_day_other(self):
        result = sundays.weekday(2012, 4, 1)
        self.assertEqual(result, 7) 
        
    def test_countSundays(self):
        result = sundays.countSundays(1901, 2000)
        self.assertEqual(result, 171)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
