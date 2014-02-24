#!/usr/bin/python
import math

def factors(n):
    factors = 0
    for d in range(1, int(math.sqrt(n))+1):
        if n % d == 0:
              factors = factors + 2
    return factors

def triangularNumber():
    found = False
    triangleNr = 1
    i = 2
    while not found:
        triangleNr = triangleNr + i;
        factorCount = factors(triangleNr)
        if factorCount > 500:
            return triangleNr
        i = i + 1
