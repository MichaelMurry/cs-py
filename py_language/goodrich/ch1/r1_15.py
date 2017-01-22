#!/usr/bin/python


def foo(n):
    y = set(n)
    if len(n) == len(y):
        print("Distinct!")
    else:
        print("Nope!")

    return

x = [1, 1, 3, 3, 5, 10]

foo(x)