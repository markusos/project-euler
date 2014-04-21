#!/usr/bin/python
fib1 = 1
fib2 = 1

def init():
    global fib1, fib2
    fib1 = 1
    fib2 = 1   

def nextFib():
    global fib1, fib2
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    return fib

def fibOfLength(length):
    init()
    i = 2
    while len(str(fib2)) < length:
        nextFib()
        i += 1
    return i
