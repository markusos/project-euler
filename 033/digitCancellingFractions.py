#!/usr/bin/python


def digit_cancelling_fractions():
    dividend_product = 1
    divisor_product = 1

    for divisor in range(10, 100):
        for dividend in range(10, divisor):
            if naive_cancellation(dividend, divisor):
                divisor_product *= divisor
                dividend_product *= dividend

    return divisor_product / gcd(dividend_product, divisor_product)


def naive_cancellation(a, b):
    dividend = str(a)
    divisor = str(b)

    # Skip all trivial cases containing 0
    if '0' in dividend or '0' in divisor:
        return False

    # Find any matching digit between dividend and divisor
    if dividend[0] == divisor[0]:
        dividend = int(dividend[1])
        divisor = int(divisor[1])
    elif dividend[0] == divisor[1]:
        dividend = int(dividend[1])
        divisor = int(divisor[0])
    elif dividend[1] == divisor[1]:
        dividend = int(dividend[0])
        divisor = int(divisor[0])
    elif dividend[1] == divisor[0]:
        dividend = int(dividend[0])
        divisor = int(divisor[1])
    else:
        return False

    quotient = dividend / divisor
    c = a / b

    # Check if naive cancellation match
    if quotient == c:
        return True
    else:
        return False


# Return greatest common divisor using Euclid's Algorithm.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

