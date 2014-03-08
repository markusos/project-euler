#!/usr/bin/python
import os

def checkGrid(grid):
    maxVal = 0
    for i in range(0,20-3):
        for j in range(0,20-3):
            l = lineSum(grid, i, j)
            r = rowSum(grid, i, j)
            dr = diagonalRight(grid, i, j)
            dl = diagonalLeft(grid, i, j)
            maxVal = max(maxVal, max(l, r, dr, dl))
    return maxVal

def readGrid():
    grid = []
    f = open(os.path.dirname(__file__) + '\\grid.txt', 'r')
    for line in f:
        grid.append([int(i) for i in line.replace('\n', '').split(" ")])
    f.close()
    return grid

def lineSum(grid, i, j):
    return grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

def rowSum(grid, i, j):
    return grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]

def diagonalRight(grid, i, j):
    return grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]

def diagonalLeft(grid, i, j):
    return grid[i+3][j] * grid[i+2][j+1] * grid[i+1][j+2] * grid[i][j+3]



