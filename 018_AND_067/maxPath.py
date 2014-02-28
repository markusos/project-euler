#!/usr/bin/python
import os

def maxPath(fileName):
    triangle =[]
    f = open(os.path.dirname(__file__) + '\\' + fileName, 'r')
    for line in f:
        triangle.append(map(int, line.replace('\n', '').split(" ")))

    length = len(triangle)
    a = []
    for i in range(0, length):
        a.append(triangle[i] + [0 for x in range(0,length - len(triangle[i]))])

    b = [[0 for x in range(0,length)] for y in range(0,length)]
    
    for i in range(0, length):
        for j in range(0, i+1):
            if i == 0:
                b[i][j] = a[i][j]
            elif j == 0:
                b[i][j] = a[i][j] + b[i-1][j]
            else:
                b[i][j] = a[i][j] + max(b[i-1][j], b[i-1][j-1])
    maxVal = 0
    
    for j in range(0, length):
        if maxVal < b[length-1][j]:
            maxVal = b[length-1][j]

    return maxVal
