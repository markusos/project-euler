#!/usr/bin/python
import math

def factorial(n):
    factorial = 1
    for i in range(2, n+1):
        factorial = factorial*i
    return factorial

def factorialSum(n):
    sum = 0
    for c in str(factorial(n)):
        sum = sum + int(c)
    return sum 
