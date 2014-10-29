#!/usr/bin/python
fib1 = 1
fib2 = 2


def init():
    global fib1, fib2
    fib1 = 1
    fib2 = 2


def nextFib():
    global fib1, fib2
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib


def evenFibSum(below):
    sum = 0
    global fib1, fib2
    while fib2 < below:
        if fib2 % 2 == 0:
            sum = sum + fib2
        nextFib()

    return sum
