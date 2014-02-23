#!/usr/bin/python
def shift(values):
    for i in range(0,4):
        values[i] = values[i+1]
    return values

def product(values):
    product = 1
    for v in values:
        product = product*v
    return product

def findValues(n):
    maxValue = 0
    numberString = n
    values = [0,0,0,0,0]
    count = 0
    for c in numberString:
        values = shift(values)
        values[4] = int(c)
        prod = product(values)
        if prod > maxValue:
            maxValue = prod

    return maxValue


 

        
