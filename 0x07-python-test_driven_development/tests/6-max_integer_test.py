#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from min_integer import min_integer

class TestMinInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(min_integer([]))

    def test_one_element_list(self):
        self.assertEqual(min_integer([5]), 5)

    def test_ordered_list(self):
        self.assertEqual(min_integer([1, 2, 3, 4, 5]), 1)

    def test_reverse_ordered_list(self):
        self.assertEqual(min_integer([5, 4, 3, 2, 1]), 1)

    def test_unordered_list(self):
        self.assertEqual(min_integer([3, 5, 1, 4, 2]), 1)

if __name__ == '__main__':
    unittest.main()
