#!/usr/bin/env python

import unittest
import sys, os

for file in os.listdir('.'):
    if os.path.isfile(file): pass
    else: sys.path.append('./' + file)

if __name__ == "__main__":
    suite = unittest.TestLoader().discover('.', pattern = "test.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
