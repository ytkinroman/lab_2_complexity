#  Задача 5.

from typing import List, Tuple
from math import atan2, sqrt
import time
import os
import psutil

# Константы.

MIN_POINTS = 5
MAX_POINTS = 500000
MIN_COORD = -10000
MAX_COORD = 10000


# Считаем затраченную память.
def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


class QuickSort:
    def __init__(self, array: List[Tuple[int, int]], s_point: Tuple[int, int]) -> None:
        self.array = array
        self.start_point = s_point

    def __polar_angle(self, point: Tuple[int, int]) -> float:
        """Вычисляет полярный угол точки p относительно начальной точки."""
        return atan2(point[1] - self.start_point[1], point[0] - self.start_point[0])

    def __quick_sort(self, low: int, high: int) -> None:
        """Алгоритм быстрой сортировки."""
        if low < high:
            mid = self.__partition(low, high)
            self.__quick_sort(low, mid - 1)
            self.__quick_sort(mid + 1, high)

    def __partition(self, low: int, high: int) -> int:
        """Функция разделения массива."""
        pivot = self.array[high]
        pivot_angle = self.__polar_angle(pivot)
        i = low - 1
        for j in range(low, high):
            if self.__polar_angle(self.array[j]) <= pivot_angle:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def sort(self) -> List[Tuple[int, int]]:
        """Сортировка массива с помощью быстрой сортировки."""
        self.__quick_sort(0, len(self.array) - 1)
        return self.array


def find_start_point(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Находит начальную точку (самую нижнюю и самую левую) из списка точек. """
    current_min_point = points[0]

    for current_point in points:
        current_y = current_point[1]
        current_x = current_point[0]

        min_y = current_min_point[1]
        min_x = current_min_point[0]

        if current_y < min_y or (current_y == min_y and current_x < min_x):
            current_min_point = current_point

    return current_min_point


def cross_product(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> float:
    """Вычисляет векторное произведение для определения поворота."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """Вычисляет векторное произведение для определения поворота."""
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def graham_scan(sorted_points: List[Tuple[int, int]], start_point: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Алгоритм Грэхема для нахождения выпуклой оболочки."""
    hull = [start_point]
    for point in sorted_points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], point) <= 0:
            hull.pop()  # Удаляем точку из списка, если она создаёт правый поворот. Если результат векторного произведения отрицательный.

        hull.append(point)
    return hull


def perimeter(hull: List[Tuple[int, int]]) -> float:
    """Вычисляет периметр выпуклой оболочки."""
    result_perimeter = 0
    for i in range(len(hull)):
        result_perimeter += distance(hull[i], hull[(i + 1) % len(hull)])
    return result_perimeter


if __name__ == "__main__":
    n = int(input())

    # Проверка на допустимое количество точек.
    if not (MIN_POINTS <= n <= MAX_POINTS):
        raise ValueError(f"Количество точек должно быть в диапазоне от {MIN_POINTS} до {MAX_POINTS}!")

    my_points = []
    for i in range(n):
        x, y = input().split()
        x, y = int(x), int(y)

        if not (MIN_COORD <= x <= MAX_COORD) or not (MIN_COORD <= y <= MAX_COORD):
            raise ValueError(f"Координаты точки должны быть в диапазоне от {MIN_COORD} до {MAX_COORD}!")

        my_points.append((x, y))

    start_time = time.perf_counter()

    start_point = find_start_point(my_points)
    # print(start_point, "точка старта")
    my_points.remove(start_point)

    sorter = QuickSort(my_points, start_point)
    sorted_points = sorter.sort()
    # sorted_points.append(start_point)
    # print(sorted_points, "точки после сортировки без стартовой точки")

    hull = graham_scan(sorted_points, start_point)
    # print("Выпуклая оболочка:", hull)

    p = perimeter(hull)
    # print("Периметр:", round(p, 2))
    print(round(p, 2))

    stop_time = time.perf_counter()

    print("=" * 42)
    print(f"    Время выполнения: {stop_time - start_time:0.5f} секунд.")
    final_memory = get_memory_usage()
    print(f"    Использовано памяти: {final_memory:.2f} Mb.")
    print("=" * 42)
