#!/usr/bin/env python
import os

class bigInt:
    number = []
    def __init__(self, numString):
        self.number = numString
        
    def getPaddedNumber(self, length):
        while len(self.number) < length:
            self.number = [0] + self.number
        return self.number

    def getNummerString(self):
         return "".join(map(str, self.number))
    
    def add(self, n):
        result = []
        mem = 0
        decSum = 0
        self.number = self.getPaddedNumber(len(n.number))
        n.number = n.getPaddedNumber(len(self.number))
        
        i = len(self.number)-1
        while i >=0:
            decSum = self.number[i] + n.number[i] + mem
            if decSum >= 10:
                mem = 1
            else:
                mem = 0
            result = [decSum % 10] + result
            i = i - 1
            
        if mem == 1:
            result = [1] + result
        self.number = result


def sumNumbers():            
    numbers = []
    f = open(os.path.dirname(__file__) + '\\numbers.txt', 'r')
    for line in f:
        numbers.append(map(int, list(line.replace('\n', ''))))

    sum = bigInt([0])

    for n in numbers:
        num2 = bigInt(n)
        sum.add(num2)

    return sum.getNummerString()

