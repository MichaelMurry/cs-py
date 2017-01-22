# R1-11. Demonstrate how to use Python's list comprehension syntax to produce the list
# [1, 2, 4, 8, 16, 32, 64, 128, 256].


#!/usr/bin/python

def foo(n):
    return [2**j for j in range(0, n)]

print(foo(9))
