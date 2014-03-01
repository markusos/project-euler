#!/usr/bin/python
import math

def divisors(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i) 
        
    return divisors

def d(n):
    return sum(divisors(n));
        
def amicableNumbers(below):
    found = set()
    for i in range(1, below):
        if i in found:
            continue
        a = d(i)
        b = d(a)
        if b == i and not a == b:
            found.add(a)
            found.add(b)
    return found 
