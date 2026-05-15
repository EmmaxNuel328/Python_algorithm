import unittest
from Minimum_rotated_sorted_array import find_min


class TestFindMin(unittest.TestCase):
    def test_find_min(self):
        numbers = [4, 5, 6, 7, 0, 1, 2]
        actual = find_min(numbers)
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_find_min_single_element(self):
        numbers = [10]
        actual = find_min(numbers)
        expected = 10
        self.assertEqual(actual, expected)  
        
    def test_find_min_sorted_array(self):
        numbers = [1, 2, 3, 4, 5]
        actual = find_min(numbers)
        expected = 1
        self.assertEqual(actual, expected)  