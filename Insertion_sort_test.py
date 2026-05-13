import unittest
from Insertion_sort import insertion_sorting



class TestInsertionSorting(unittest.TestCase):
    def test_insertion_sorting(self):
        example = [(1, "apple"), (3, "banana"), (2, "cherry")]
        actual = insertion_sorting(example)
        expected = [[(1, "apple"), (3, "banana"), (2, "cherry")],
                    [(1, "apple"), (3, "banana"), (2, "cherry")],
                    [(1, "apple"), (2, "cherry"), (3, "banana")]
                    ]
        self.assertEqual(actual, expected)