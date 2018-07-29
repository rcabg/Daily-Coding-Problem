#!/usr/bin/env python

__author__ = "Rafael Caballero"

# Problem: Given an array of integers,
# return a new array such that each element
# at index i of the new array is the product
# of all the numbers in the original array
# except the one at i.

# Example1: if our input was [1, 2, 3, 4, 5],
#           the expected output would be [120, 60, 40, 30, 24]

# Example2: if our input was [3, 2, 1],
#           the expected output would be [2, 3, 6].

from functools import reduce

def get_new_array_mul(array):
    if not array:
        return []

    total_mul = reduce(lambda x, y: x*y, array)
    new_array = list()
    for i in array:
        new_array.append(total_mul/i)
    return  new_array

def get_new_array_mul_no_div(array): #using no division
    if not array:
        return []

    new_array = list()
    for i in range(len(array)):
        count = 0
        total = 1
        for element in array:
            if i == count:
                count += 1
                continue
            else:
                total *= element
                count += 1
        new_array.append(total)
    return new_array


