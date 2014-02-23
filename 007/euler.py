#!/usr/bin/python

def euler(nr):
    primes = [2,3,5,7]
    examine = 10
    while len(primes) < nr:
        prime = True
        for p in primes:
            if examine % p == 0:
                prime = False
                break
        if prime:
            primes.append(examine)

        examine = examine + 1

    return primes



        

