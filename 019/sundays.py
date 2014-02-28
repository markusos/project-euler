#!/usr/bin/python

def isLeapYear(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False
    
# Returns 1 for Monday, 2 for Tuesday, ... 7 for Friday
def weekday(y, m, d):
    m -= 1
    d -= 1
    days = 0
    for i in range(1900, y):
        if isLeapYear(i):
            days += 366
        else:
            days += 365

    for i in range(0, m):
        if i == 1:
            days += 28
            if isLeapYear(y):
                days += 1
        elif i == 8 or i == 3 or i == 5 or i == 10:
            days += 30
        else:
            days += 31
        
    day = (days + d) % 7
    return day+1

# Count Sundays that occure on the 1:th of the month
# between 1 Jan of startYear to 31 Dec of endYear
def countSundays(startYear, endYear):  
    sundays = 0
    for y in range(startYear, endYear+1):
        for m in range(1,13):
            if weekday(y,m,1) == 7:
                sundays += 1

    return sundays
