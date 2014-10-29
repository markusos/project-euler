#!/usr/bin/python


def find_optimal_quadratic_primes(limit):
    opt_n = 0
    opt_a = 0
    opt_b = 0

    for a in range(-limit, limit):
        for b in range(-limit, limit):
            n = count_consecutive_primes(a, b)
            if n > opt_n:
                opt_n = n
                opt_a = a
                opt_b = b

    return opt_a, opt_b


def count_consecutive_primes(a, b):
    quad = b
    n = 0
    while is_prime(quad):
        n += 1
        quad = n * n + n * a + b

    return n


# naive prime test
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
