#!/usr/bin/env python

__author__ = "Rafael Caballero"

# Problem: Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.

# Example: Given [10, 15, 3, 7] and k = 17, return true.

def is_there_a_pair_that_add_k(list_of_numbers, k):

    if not list_of_numbers:
        return False

    if k <= 0:
        return False

    numbers = set(list_of_numbers)

    for number in list_of_numbers:
        rest = k - number
        if rest in numbers:
            return True
    return False
