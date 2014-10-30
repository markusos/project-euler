#!/usr/bin/python


def count_9_pandigit():
    products = set()

    for a in range(1, 100):
        for b in range(1,5000):
            p = a * b
            if is_9_pandigit(str(a) + str(b) + str(p)):
                products.add(p)

    product_sum = 0
    for p in products:
        product_sum += p

    return product_sum


def is_9_pandigit(number):
    if len(number) != 9:
        return False

    number_set = set(number)

    if len(number_set) != 9:
        return False
    elif '0' in number_set:
        return False
    else:
        return True