#!/usr/bin/python

# fractionCycle finds the recurring cycle of
# the decimals in a fraction 1 / divisor
# returns the decimals in the cycle or '' if none exists
def fractionCycle(divisor):
    dividend = 10
    decimals = ''
    states = {}
    
    while dividend > 0:
        states[dividend] = len(decimals)
        
        v = dividend // divisor
        dividend = 10 * (dividend - v * divisor)
        decimals += str(v)

        previousState = states.get(dividend)
        if previousState != None:
            return decimals[previousState:]
        
    return ''

# longestCycle finds the longest recurring
# cycle of decimals in a number 1 / d for d < limit
def longestCycle(limit):
    longestFound = 0
    value = 0
    for d in range(2, limit):
        length = len(fractionCycle(d))
        if length > longestFound:
            longestFound = length
            value = d

    return value
