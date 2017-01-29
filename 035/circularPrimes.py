#!/usr/bin/python
import math
import collections


def find_circular_primes(below):
    prime_numbers = set(primes(below))
    circular_primes = []
    for prime in prime_numbers:
        prime_rotations = rotations(prime)
        circular_prime = True
        for number in prime_rotations:
            if number not in prime_numbers:
                circular_prime = False
                break

        if circular_prime:
            circular_primes.append(prime)

    return circular_primes


# Get all rotations for the given number
# 123 -> [123, 231, 312]
def rotations(num):
    d = collections.deque(str(num))
    rotations = []
    for i in range(0, len(d)):
        rotations.append(int(''.join(d)))
        d.rotate(-1)

    return rotations


# Finds all primes below the given number
def primes(below):
    prime_numbers = [2]
    examine = 3
    while examine < below:
        prime = True
        for p in prime_numbers:
            if p > int(math.sqrt(examine) + 1):
                break
            if examine % p == 0:
                prime = False
                break
        if prime:
            prime_numbers.append(examine)

        examine += 1

    return prime_numbers

