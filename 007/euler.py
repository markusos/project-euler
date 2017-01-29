#!/usr/bin/python
import math


def euler(nr):
    primes = [2]
    examine = 3
    while len(primes) < nr:
        prime = True
        for p in primes:
            if p > int(math.sqrt(examine) + 1):
                break
            if examine % p == 0:
                prime = False
                break
        if prime:
            primes.append(examine)

        examine += 1

    return primes
