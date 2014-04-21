#!/usr/bin/python
import itertools


def permutation(i, data):
    return list(map(lambda x: ''.join(x), list(itertools.permutations(data))))[i]
