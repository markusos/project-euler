#!/usr/bin/python


def is_palindrome(nr):
    number = str(nr)
    mirrored_number = number[::-1]
    if number == mirrored_number:
        return True
    else:
        return False


def is_double_based_palindrome(nr):
    return is_palindrome(nr) and is_palindrome(bin(nr)[2:])


def sum_double_based_palindromes(below):
    sum = 0
    for nr in range(0, below):
        if is_double_based_palindrome(nr):
            sum += nr

    return sum
