from typing import List, Tuple
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


class QuickSort:
    def __init__(self, array: List[Tuple[str, List[int]]], priorities: List[int]) -> None:
        self.array = array
        self.priorities = priorities

    def __quick_sort(self, low: int, high: int) -> None:
        if low < high:
            mid = self.__partition(low, high)
            self.__quick_sort(low, mid - 1)
            self.__quick_sort(mid + 1, high)

    def __partition(self, low: int, high: int) -> int:
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.__compare(self.array[j], pivot):
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def __compare(self, item1: Tuple[str, List[int]], item2: Tuple[str, List[int]]) -> bool:
        for priority in self.priorities:
            if item1[1][priority - 1] > item2[1][priority - 1]:
                return True
            elif item1[1][priority - 1] < item2[1][priority - 1]:
                return False
        return False

    def sort(self) -> List[Tuple[str, List[int]]]:
        self.__quick_sort(0, len(self.array) - 1)
        return self.array


def main():
    N = int(input())
    k = int(input())
    priorities_str = input().split()
    priorities = []
    for p in priorities_str:
        priorities.append(int(p))

    records = []
    for _ in range(N):
        line = input().split()
        name = line[0]
        values = []
        for v in line[1:]:
            values.append(int(v))
        records.append((name, values))

    # Запуск таймера
    start_time = time.perf_counter()

    sorter = QuickSort(records, priorities)
    sorted_records = sorter.sort()

    for record in sorted_records:
        print(record[0])

    stop_time = time.perf_counter()

    # Вывод времени выполнения
    print("=" * 42)
    print(f"    Время выполнения: {stop_time - start_time:0.5f} секунд.")
    # Получение и вывод используемой памяти
    final_memory = get_memory_usage()
    print(f"    Использовано памяти: {final_memory:.2f} Mb.")
    print("=" * 42)


if __name__ == "__main__":
    main()
