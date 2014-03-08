#!/usr/bin/python
import numberToLetter 
import unittest

class TestNumberToLetter(unittest.TestCase):

    def test_numberToLetter_342(self):
        result = numberToLetter.numberToLetters(342)
        self.assertEqual(result, "three hundred and forty-two")
        result = len(result.replace(" ", "").replace("-", ""))
        self.assertEqual(result, 23)
    def test_numberToLetter_115(self):
        result = numberToLetter.numberToLetters(115)
        self.assertEqual(result, "one hundred and fifteen")
        result = len(result.replace(" ", "").replace("-", ""))
        self.assertEqual(result, 20)
        
    def test_numberToLetter_count(self):
        result = numberToLetter.countLetters(range(1, 1001))
        self.assertEqual(result, 21124)
        print("Result: {0}".format(result))

if __name__ == '__main__':
    unittest.main()
