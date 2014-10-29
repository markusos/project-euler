#!/usr/bin/python
def checkPalindrom(nr):
    number = str(nr)
    palindrom = number[::-1]
    if number == palindrom:
        return True
    else:
        return False


def largestPalindromFromProduct(productsBelow):
    largestPalindrom = 0
    for a in range(1, productsBelow):
        for b in range(1, productsBelow):
            product = a * b
            if checkPalindrom(product):
                if product > largestPalindrom:
                    largestPalindrom = product
    return largestPalindrom