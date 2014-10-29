#!/usr/bin/python
import math


def digitPowers(powers):
    found = set()

    limit = determineLimit(powers)

    for nr in range(2, int(limit)):
        digits = [int(i) for i in str(nr)]
        sum = 0
        for digit in digits:
            sum += math.pow(digit, powers)

        if sum == nr:
            found.add(nr)

    return found


def determineLimit(powers):
    limit = 0
    number = 0
    i = 1

    while number <= limit:
        limit += math.pow(9, powers)
        number += math.pow(10, i)
        i += 1

    return limit


def digitPowersSum(powers):
    result = digitPowers(powers)
    sum = 0
    for i in result:
        sum += i
    return sum
