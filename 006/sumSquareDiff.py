#!/usr/bin/python

def sumSquareDiff(number):
    sumNat = 0
    sumSquere = 0

    for i in range(1, number+1):
        sumNat = sumNat + i
        sumSquere = sumSquere + i*i

    sumNatSquare = sumNat*sumNat

    dif = abs(sumNatSquare - sumSquere)
    return dif
