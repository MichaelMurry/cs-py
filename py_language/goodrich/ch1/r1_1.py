# R1-1.1: Write a short Python function, is_multiple(n,m), that takes two integer
# values and returns True if n is a multiple of m, that is,  n=mi for some integer i,
# and False otherwise.

#!/usr/bin/python


def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

print(is_multiple(10, 5))

