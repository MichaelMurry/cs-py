# R-1.7: Give a single command that computes the sum from Exercise R-1.6, relying
# on Python's comprehension syntax and the built-in sum function

#!/usr/bin/python

def sum_of_squares_odd2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares_odd2(4))
