#!/usr/bin/python
import math


def is_pandigital(number):

    number_string = str(number)

    if len(number_string) != 9:
        return False

    for i in range(1, 9):
        if str(i) not in number_string: 
        	return False

    return True


def is_pandigital_base(base):

	max_theoretical_pandigital = 987654321
	concatenated_products = base
	n = 2
	
	while concatenated_products < max_theoretical_pandigital:
		concatenated_products = int(str(concatenated_products) + str(base * n))

		if is_pandigital(concatenated_products):
			return concatenated_products

		n += 1

	return False


def max_pandigital():
	
	max_base = 9999 # len("10000" + "20000") > 9
	max_pandigital_found = 0
	base = 1

	while base < max_base:
		pandigital = is_pandigital_base(base)
		if pandigital and pandigital > max_pandigital_found:
			max_pandigital_found = pandigital

		base += 1

	return max_pandigital_found
