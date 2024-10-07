import unittest
from q_8 import MuseumVisitors


class TestCase(unittest.TestCase):
    def test_max_visitors_1(self):
        """1. Тестирование на максимальное количество посетителей."""
        intervals = [
            [(10, 0), (12, 0)],
            [(9, 0), (11, 0)],
            [(11, 0), (13, 0)]
        ]
        museum = MuseumVisitors(intervals)
        max_visitors = museum.find_max_visitors()
        self.assertEqual(max_visitors, 3)

    def test_max_visitors_2(self):
        """2. Тестирование на максимальное количество посетителей."""
        intervals = [
            [(9, 0), (10, 7)],
            [(10, 20), (11, 35)],
            [(12, 0), (17, 0)],
            [(11, 0), (11, 30)],
            [(11, 20), (12, 30)],
            [(11, 30), (18, 15)],
            [(11, 50), (12, 15)],
            [(11, 30), (18, 0)]
        ]
        museum = MuseumVisitors(intervals)
        max_visitors = museum.find_max_visitors()
        self.assertEqual(max_visitors, 5)

    def test_max_visitors_3(self):
        """3. Тестирование на максимальное количество посетителей."""
        intervals = [
            [(9, 0), (10, 7)],
            [(10, 20), (11, 35)],
            [(12, 0), (17, 0)],
            [(11, 0), (11, 30)],
            [(11, 20), (12, 30)],
            [(11, 30), (18, 15)],
        ]
        museum = MuseumVisitors(intervals)
        max_visitors = museum.find_max_visitors()
        self.assertEqual(max_visitors, 4)

    def test_max_visitors_4(self):
        """4. Тестирование на максимальное количество посетителей."""
        intervals = [
            [(9, 0), (9, 30)],
            [(10, 0), (12, 0)],
            [(9, 0), (11, 0)]
        ]
        museum = MuseumVisitors(intervals)
        max_visitors = museum.find_max_visitors()
        self.assertEqual(max_visitors, 2)
