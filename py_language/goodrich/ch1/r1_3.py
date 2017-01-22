# R-1.3: Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
# and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use
# the built-in functions min or max in implementing your solution

#!/usr/bin/python

def minmax(data):
    min_index = 0
    max_index = 0

    for j in range(1, len(data)):
        if data[j] > data[max_index]:
            max_index = j

        if data[j] < data[min_index]:
            min_index = j

    return data[max_index], data[min_index]


numbers = [1,3,5,10,11]

print(minmax(numbers))
