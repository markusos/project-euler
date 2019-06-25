#!/usr/bin/python
import math	

# Test if a, b, c makes a Pythagorean triple
def is_pythagorean_triple(a, b, c):
	return (a * a + b * b == c * c)

# Generate all Pythagorean triples up to p_max
def pythagorean_triples(p_max):
	triples = {}

	for a in range(1, int(p_max/2)):
		for b in range(a + 1, int(p_max/2)):
			c = int(math.sqrt(a*a + b*b))
			p = a + b + c
			if p not in triples:
				triples[p] = []
			if is_pythagorean_triple(a, b, c):
				triples[p].append([a, b, c])

	return triples

def max_pythagorean_triples(p_max):
	triples_max = 0
	p_triples_max = 0

	triples = pythagorean_triples(p_max)

	for p in range(1, p_max):
		count = len(triples.get(p, []))
		if count > triples_max:
			triples_max = count
			p_triples_max = p

	return p_triples_max
