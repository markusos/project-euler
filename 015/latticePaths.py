#!/usr/bin/python

def latticePaths(number):
    a =[[0 for x in range(0,number+1)] for y in range(0, number+1)]
    for i in range(0,number+1):
        for j in range(0,number+1):
            if i == 0 or j == 0:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j] +  a[i][j - 1]

    return a[number][number]
