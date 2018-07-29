#!/usr/bin/env python

__author__ = "Rafael Caballero"

import unittest

import problem_07_28_2018 as src

class TestProblemMethods(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(src.is_there_a_pair_that_add_k([], 17))

    def test_zero_k(self):
        self.assertFalse(src.is_there_a_pair_that_add_k([3, 19, 5], 0))

    def test_negative_k(self):
        self.assertFalse(src.is_there_a_pair_that_add_k([3, 19, 5], -5))

    def test_false_case_0(self):
        self.assertFalse(src.is_there_a_pair_that_add_k([1, 4, 5, 10], 40))

    def test_false_case_1(self):
        self.assertFalse(src.is_there_a_pair_that_add_k([1, 4, 5, 30, 10], 55))

    def test_true_case_0(self):
        self.assertTrue(src.is_there_a_pair_that_add_k([10, 15, 3, 7], 17))

    def test_true_case_1(self):
        self.assertTrue(src.is_there_a_pair_that_add_k([10, 15, 3, 7, 20, 14, 9], 24))

if __name__ == '__main__':
    unittest.main()
