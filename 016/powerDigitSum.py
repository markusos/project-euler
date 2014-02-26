import math
def powerDigitSum(power):
    sum = 0
    p = power
    n = str(2 << p-1)
    for c in n:
        sum = sum + int(c)

    return sum

