#!/usr/bin/python
import math


def eratosthenes(n):
    primes = []
    numbers = [True] * n

    for i in range(2, int(math.sqrt(n) + 1)):
        if numbers[i]:
            for j in range(i * i, n, i):
                numbers[j] = False

    for i in range(2, n):
        if numbers[i]:
            primes.append(i)

    return primes


def primeSum(number):
    sum = 0
    for p in eratosthenes(number):
        sum = sum + p
    return sum
