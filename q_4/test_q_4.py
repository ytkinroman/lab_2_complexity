import unittest
from q_4 import QuickSort


class TestCase(unittest.TestCase):
    def test_sort_1(self):
        """1. Тестирование."""
        priorities = [2, 1, 3]
        records = [
            ("A", [1, 2, 3]),
            ("B", [3, 2, 1]),
            ("C", [3, 1, 2])
        ]
        expected_output = [("B", [3, 2, 1]), ("A", [1, 2, 3]), ("C", [3, 1, 2])]

        sorter = QuickSort(records, priorities)
        sorted_records = sorter.sort()

        self.assertEqual(sorted_records, expected_output)

    def test_sort_2(self):
        """2. Тестирование."""
        priorities = [1, 2]
        records = [
            ("A", [1, 2]),
            ("B", [2, 1]),
            ("C", [3, 3]),
            ("D", [4, 4])
        ]
        expected_output = [('D', [4, 4]), ('C', [3, 3]), ('B', [2, 1]), ('A', [1, 2])]

        sorter = QuickSort(records, priorities)
        sorted_records = sorter.sort()

        self.assertEqual(sorted_records, expected_output)

    def test_sort_3(self):
        """3. Тестирование."""
        priorities = [3, 1, 2]
        records = [
            ("A", [1, 2, 3]),
            ("B", [2, 3, 1]),
            ("C", [3, 1, 2]),
            ("D", [4, 4, 4]),
            ("E", [5, 5, 5])
        ]
        expected_output = [('E', [5, 5, 5]), ('D', [4, 4, 4]), ('A', [1, 2, 3]), ('C', [3, 1, 2]), ('B', [2, 3, 1])]

        sorter = QuickSort(records, priorities)
        sorted_records = sorter.sort()

        self.assertEqual(sorted_records, expected_output)

    def test_sort_4(self):
        """4. Тестирование."""
        priorities = [2, 1]
        records = [
            ("A", [1, 2]),
            ("B", [2, 1])
        ]
        expected_output = [('A', [1, 2]), ('B', [2, 1])]

        sorter = QuickSort(records, priorities)
        sorted_records = sorter.sort()

        self.assertEqual(sorted_records, expected_output)
