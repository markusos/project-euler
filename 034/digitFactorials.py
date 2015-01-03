#!/usr/bin/python
import math

def is_digit_factorial(number):

    sum = 0
    number_string = str(number)

    if len(number_string) == 1:
        return False

    for i in number_string:
        sum += math.factorial(int(i))

    return sum == number

def find_digit_factorial(max):

    digit_factorials = []

    for i in range(0, max):
        if(is_digit_factorial(i)):
            digit_factorials.append(i)

    return digit_factorials;



