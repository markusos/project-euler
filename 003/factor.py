#!/usr/bin/python

# Pollard's rho algorithm
def pollard_rho(n):
  x = 2
  y = 2
  d = 1
  while d == 1:
    x = f(x, n)
    y = f(f(y, n), n)
    d = gcd(abs(x-y), n)
  if (d == n):
    return 0
  else:
    return d

def f(x, n):
  return (x*x + 1) % n

# Greatest common divisor	
def gcd(a, b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

def factors(n):
  factorList = []
  factor = pollard_rho(n)
  if factor != 0:
    factorList += factors(n/factor)
    factorList += factors(factor)
  else:
    return [n]
  
  return factorList
