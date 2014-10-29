#!/usr/bin/python
import sequence
import unittest


class TestSequence(unittest.TestCase):
    def test_sequence(self):
        result = sequence.sequence(13)
        self.assertEqual(result, 10)

    def test_sequence_longestCollatzSequence(self):
        result = sequence.longestCollatzSequence()
        self.assertEqual(result, 837799)
        print("Result: {0}".format(result))


if __name__ == '__main__':
    unittest.main()
