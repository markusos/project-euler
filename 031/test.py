#!/usr/bin/python
import coinSum
import unittest


class TestCoinSum(unittest.TestCase):
    def test_coin_sum_small1(self):
        result = coinSum.coin_sum_combinations(2)
        # 2p can only be made op of either 1p*2 or 2p coins
        self.assertEqual(result, 2)

    def test_coin_sum_small2(self):
        result = coinSum.coin_sum_combinations(4)
        # 4p can only be made op of either 1p*4, 2p*2 or 1p+2 + 2p coins
        self.assertEqual(result, 3)

    def test_coin_sum(self):
        result = coinSum.coin_sum_combinations(200)
        self.assertEqual(result, 73682)
        print("Result: {0}".format(result))



if __name__ == '__main__':
    unittest.main()