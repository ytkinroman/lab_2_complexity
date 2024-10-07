import unittest
from q_9 import QuickSort, SecurityTestChecker


class TestQuickSort(unittest.TestCase):
    def test_sort_empty_array(self):
        qs = QuickSort([])
        self.assertEqual(qs.sort(), [])

    def test_sort_single_element(self):
        qs = QuickSort([5])
        self.assertEqual(qs.sort(), [5])

    def test_sort_sorted_array(self):
        qs = QuickSort([1, 2, 3, 4, 5])
        self.assertEqual(qs.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted_array(self):
        qs = QuickSort([5, 4, 3, 2, 1])
        self.assertEqual(qs.sort(), [1, 2, 3, 4, 5])

    def test_sort_random_array(self):
        qs = QuickSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.assertEqual(qs.sort(), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_run_tests_1(self):
        lines = ["2", "3 0 3000 2500 7000 2700 10000", "2 0 3000 2700 10000"]
        checker = SecurityTestChecker(2, lines[1:])
        result = checker.run_tests()
        self.assertEqual(result, "Wrong Answer\nAccepted")

    def test_run_tests_2(self):
        lines = ["1", "2 0 3000 2700 9000"]
        checker = SecurityTestChecker(1, lines[1:])
        result = checker.run_tests()
        self.assertEqual(result, "Wrong Answer")

    def test_run_tests_3(self):
        lines = ["1", "3 0 3000 2500 7000 2700 10000"]
        checker = SecurityTestChecker(1, lines[1:])
        result = checker.run_tests()
        self.assertEqual(result, "Wrong Answer")

    def test_run_tests_4(self):
        lines = ["1", "3 0 3000 2500 7000 2700 10000"]
        checker = SecurityTestChecker(1, lines[1:])
        result = checker.run_tests()
        self.assertEqual(result, "Wrong Answer")