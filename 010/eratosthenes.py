#!/usr/bin/python

def eratosthenes(maxNr):
    primes = []
    numbers = range(2, maxNr)
    notPrime = set()
    i = 0
    while i < len(numbers):
        a = numbers[i]
        if a not in notPrime:
            primes.append(a)
        j = i + 1
        for j in xrange(numbers[i], maxNr, a):
            notPrime.add(j)
        i = i + 1
    return primes

def primeSum(number):
    sum = 0
    for p in eratosthenes(number):
        sum = sum + p
    return sum
