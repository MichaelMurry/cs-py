# R-1.4: Write a short python function that takes a positive integer n and returns the sum of the squares
# of all the positive integers smaller than n.

#!/usr/bin/python


def foo(n):
    return sum([k*k for k in range(0, n)])


num = 5

print(foo(num))
