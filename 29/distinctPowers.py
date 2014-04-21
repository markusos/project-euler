#!/usr/bin/python
import math

        
def distinctPowers(maxBase, maxPower):
    found = set()
    for a in range(2, maxBase+1):
        for b in range(2, maxPower+1):
            res = math.pow(a, b)
            found.add(res)

    return len(found)
