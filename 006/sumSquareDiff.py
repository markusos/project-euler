#!/usr/bin/python


def sumSquareDiff(number):
    sumNat = 0
    sumSquare = 0

    for i in range(1, number + 1):
        sumNat += i
        sumSquare += i * i

    sumNatSquare = sumNat * sumNat

    dif = abs(sumNatSquare - sumSquare)
    return dif
