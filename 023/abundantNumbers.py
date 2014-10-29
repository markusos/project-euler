#!/usr/bin/python
import os
import math


def nonAbundantNumberSum():
    result = 0
    limit = 28123
    abundant = abundantNumbers(limit)
    for i in range(0, limit):
        if not isAbundantNumberSum(i, abundant):
            result += i
    return result


def abundantNumbers(limit):
    abundant = set()
    for i in range(12, limit):
        if i < sum(divisors(i)):
            abundant.add(i)
    return abundant


def isAbundantNumberSum(number, abundant):
    for i in abundant:
        if i >= number:
            return False
        if number - i in abundant:
            return True
    return False


def divisors(n):
    divisors = {1}
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return divisors    


