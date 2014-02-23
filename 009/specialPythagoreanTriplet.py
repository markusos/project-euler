#!/usr/bin/python

def specialPythagoreanTriplet():
    for c in range(1, 1000):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == 1000:
                    if pythagorean(a, b, c):
                        return a*b*c

def pythagorean(a, b, c):
    if(a*a + b*b == c*c):
        return True
    else:
        return False
                    
