#!/usr/bin/python
def multiples(multiples, below):
    sum = 0
    for i in range(0, below):
        for m in multiples:
            if i % m == 0:
                sum += i
                break;
            
    return sum
