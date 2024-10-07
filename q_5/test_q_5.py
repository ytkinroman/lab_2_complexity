import unittest
from q_5 import find_start_point, QuickSort, graham_scan, perimeter


class TestCase(unittest.TestCase):
    def test_find_start_point(self):
        """1. Тестирование на поиск начальной точки."""
        self.assertEqual(find_start_point([(2, 1), (2, 2), (2, 3), (3, 2), (1, 2)]), (2, 1))          # 5.
        self.assertEqual(find_start_point([(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]), (0, -1))       # 5.
        self.assertEqual(find_start_point([(0, 1), (1, 1), (1, 0), (2, 1), (3, 2), (1, 2)]), (1, 0))  # 6.
        self.assertEqual(find_start_point([(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]), (0, 0))  # 8.

    def test_quick_sort_1(self):
        """2. Тестирование на сортировку."""
        points = [(2, 2), (2, 3), (3, 2), (1, 2)]
        pivot = (2, 1)
        expected_sorted_points = [(3, 2), (2, 3), (2, 2), (1, 2)]
        quick_sort = QuickSort(points, pivot)
        sorted_points = quick_sort.sort()
        self.assertEqual(sorted_points, expected_sorted_points)

    def test_quick_sort_2(self):
        """2. Тестирование на сортировку."""
        points = [(1, 0), (0, 1), (-1, 0), (0, 0)]
        pivot = (0, -1)
        expected_sorted_points = [(1, 0), (0, 1), (0, 0), (-1, 0)]
        quick_sort = QuickSort(points, pivot)
        sorted_points = quick_sort.sort()
        self.assertEqual(sorted_points, expected_sorted_points)

    def test_quick_sort_3(self):
        """2. Тестирование на сортировку."""
        points = [(0, 1), (1, 1), (2, 1), (3, 2), (1, 2)]
        pivot = (1, 0)
        expected_sorted_points = [(2, 1), (3, 2), (1, 1), (1, 2), (0, 1)]
        quick_sort = QuickSort(points, pivot)
        sorted_points = quick_sort.sort()
        self.assertEqual(sorted_points, expected_sorted_points)

    def test_graham_scan_1(self):
        """3. Тестирование на правильность работы алгоритма Ерохима."""
        sorted_points = [(3, 2), (2, 3), (2, 2), (1, 2)]
        start_point = (2, 1)
        test_hull = [(2, 1), (3, 2), (2, 3), (1, 2)]

        hull = graham_scan(sorted_points, start_point)
        self.assertEqual(hull, test_hull)

    def test_graham_scan_2(self):
        """3. Тестирование на правильность работы алгоритма Ерохима."""
        sorted_points = [(1, 0), (0, 1), (-1, 0)]
        start_point = (0, -1)
        test_hull = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        hull = graham_scan(sorted_points, start_point)
        self.assertEqual(hull, test_hull)

    def test_graham_scan_3(self):
        """3. Тестирование на правильность работы алгоритма Ерохима."""
        sorted_points = [(2, 1), (3, 2), (1, 1), (1, 2), (0, 1)]
        start_point = (1, 0)
        test_hull = [(1, 0), (3, 2), (1, 2), (0, 1)]

        hull = graham_scan(sorted_points, start_point)
        self.assertEqual(hull, test_hull)

    def test_result_1(self):
        """4. Тестирование на результат работы алгоритма Ерохима."""
        hull = [(2, 1), (3, 2), (2, 3), (1, 2)]
        res_perimeter = 5.66
        p = round(perimeter(hull), 2)
        self.assertEqual(p, res_perimeter)

    def test_result_2(self):
        """4. Тестирование на результат работы алгоритма Ерохима."""
        hull = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        res_perimeter = 5.66
        p = round(perimeter(hull), 2)
        self.assertEqual(p, res_perimeter)

    def test_result_3(self):
        """4. Тестирование на результат работы алгоритма Ерохима."""
        hull = [(1, 0), (3, 2), (1, 2), (0, 1)]
        res_perimeter = 7.66
        p = round(perimeter(hull), 2)
        self.assertEqual(p, res_perimeter)
