#!/usr/bin/env python

__author__ = "Rafael Caballero"

import unittest

import problem_07_29_2018 as src

class TestProblemMethods(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(src.get_new_array_mul([]),
                         [])

    def test_example1(self):
        self.assertEqual(src.get_new_array_mul([1, 2, 3, 4, 5]),
                         [120, 60, 40, 30, 24])

    def test_example2(self):
        self.assertEqual(src.get_new_array_mul([3, 2, 1]),
                         [2, 3, 6])

    def test_empty_input_no_div(self):
        self.assertEqual(src.get_new_array_mul([]),
                         [])

    def test_example1_no_div(self):
        self.assertEqual(src.get_new_array_mul_no_div([1, 2, 3, 4, 5]),
                         [120, 60, 40, 30, 24])

    def test_example2_no_div(self):
        self.assertEqual(src.get_new_array_mul_no_div([3, 2, 1]),
                         [2, 3, 6])


if __name__ == '__main__':
    unittest.main()
