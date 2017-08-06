#!/usr/bin/python
import math


def truncatable_primes_sum(number):
    sum = 0
    for p in find_truncatable_primes(number):
        sum = sum + p
    return sum


def find_truncatable_primes(n):
    truncatable_primes = []

    primes, numbers = eratosthenes(n)

    for i in primes:
        if is_truncatable_prime(i, numbers):
            truncatable_primes.append(i)

    return truncatable_primes


def eratosthenes(n):
    primes = []
    numbers = [True] * n
    numbers[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if numbers[i]:
            for j in range(i * i, n, i):
                numbers[j] = False

    for i in range(2, n):
        if numbers[i]:
            primes.append(i)

    return primes, numbers


def is_truncatable_prime(number, is_prime):
    if len(str(number)) > 1 \
            and is_prime[number] \
            and is_truncatable_prime_left(number, is_prime) \
            and is_truncatable_prime_right(number, is_prime):
        return True
    else:
        return False


def is_truncatable_prime_left(number, is_prime):
    if len(str(number)) == 1 and is_prime[number]:
        return True
    elif len(str(number)) > 1 \
            and is_prime[number] \
            and is_truncatable_prime_left(int(str(number)[1:]), is_prime):
        return True
    else:
        return False


def is_truncatable_prime_right(number, is_prime):
    if len(str(number)) == 1 and is_prime[number]:
        return True
    elif len(str(number)) > 1 \
            and is_prime[number] \
            and is_truncatable_prime_right(int(str(number)[:-1]), is_prime):
        return True
    else:
        return False
