#!/usr/bin/python
import os

def readNames():
    names = []
    f = open(os.path.dirname(__file__) + '\\names.txt', 'r')
    for line in f:
        names += line.split(",")

    names = map(lambda each:each.strip("\""), names)
    return names

def namesScores():
    totalScore = 0
    names = sorted(readNames())
    for i in range(0, len(names)):
        totalScore +=  stringScore(names[i])*(i + 1)   
        
    return totalScore

def stringScore(string):
    score = 0
    for c in string.lower():
        score += ord(c) - 96   
    
    return score


