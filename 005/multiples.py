#!/usr/bin/python

def multiples(number):      
    factors = []
    for i in range(1, number+1):
        factors = checkfactors(factors, i)

    result = 1;
    for f in factors:
        result *= f
    return result

def checkfactors(f, n):
    allFactors = [] + f;
    numberFactors = factors(n)
    for a in numberFactors:
        if a in allFactors:
            allFactors.remove(a)
        else:
            f.append(a)
    return f

def factors(n):
    f = []
    if isPrime(n):
        return [n]
    for i in range(2, n):
        if n % i == 0:
            f = f + factors(i)
            f = f + factors(n/i)
            return f

def isPrime(n):
    primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]
    for p in primes:
        if n == p:
            return True
    return False


    

    



