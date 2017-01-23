# C-1.14: Write a short Python function that takes a sequence of integer values and determines if there is a distinct
# pair of numbers in the sequence whose product is odd


#!/usr/bin/python


def find_odd_product_pair(data):
    count = 0

    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1

    return True if count >= 2 else False

test_input = [2, 4, 6, 8]
print('Test Output: ')
print(find_odd_product_pair(test_input))
