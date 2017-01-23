# C-1.15: Write a Python function that takes a sequence of numbers and determines if all the numbers are different from
# each other (that is, they are distinct)


#!/usr/bin/python


def find_unique(data):
    tmp = []

    for k in data:
        if k in tmp:
            return False
        else:
            tmp.append(k)

    return True

test_input = [1, 3, 3, 4]
print(find_unique(test_input))
