#!/usr/bin/python


# function takes the target value in pence.
def coin_sum_combinations(value):
    # coin values in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combinations = [0] * (value + 1)
    combinations[0] = 1

    for i in range(0, len(coins)):
        for j in range(coins[i], value + 1):
            combinations[j] += combinations[j - coins[i]]

    return combinations.pop()