#!/bin/usr/python
import itertools

x = ["x", "1", "y"]
y = ["a", "b", "c"]
for L in range(0, len(x)+1):
    for subset in itertools.combinations(x, L):
	print(subset)
	
