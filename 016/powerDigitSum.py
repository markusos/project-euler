def powerDigitSum(power):
    sum = 0
    p = power
    n = str(2 << p - 1)
    for c in n:
        sum += int(c)

    return sum

