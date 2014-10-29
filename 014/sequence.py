#!/usr/bin/python
import math

sequenceLength = {}


def nextNumber(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def sequence(start):
    global sequenceLength
    seq = [1]
    n = start

    while n != 1 and n not in sequenceLength:
        seq.append(n)
        n = nextNumber(n)

    if n in sequenceLength:
        length = len(seq) + sequenceLength[n]
    else:
        length = len(seq)

    l = length
    for n in seq:
        sequenceLength[n] = l
        l -= 1

    return length


def longestCollatzSequence():
    longest = 0
    start = 0
    for n in range(1, 1000000):
        l = sequence(n)
        if l > longest:
            longest = l
            start = n
    return start
