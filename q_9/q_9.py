from typing import List
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


class QuickSort:
    def __init__(self, array: List[int]) -> None:
        self.array = array

    def __quick_sort(self, low: int, high: int) -> None:
        if low < high:
            mid = self.__partition(low, high)
            self.__quick_sort(low, mid - 1)
            self.__quick_sort(mid + 1, high)

    def __partition(self, low: int, high: int) -> int:
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def sort(self) -> List[int]:
        self.__quick_sort(0, len(self.array) - 1)
        return self.array


class SecurityTestChecker:
    def __init__(self, test_count, test_lines):
        self.test_count = test_count
        self.test_lines = test_lines
        self.results = [""] * test_count

    def __parse_line(self, line):
        parts = line.split()

        numbers = []
        for part in parts:
            number = int(part)
            numbers.append(number)

        return numbers

    def __process_events(self, numbers):
        segment_count = numbers[0]
        events = [0] * (2 * segment_count)
        for i in range(1, len(numbers), 2):
            events[i-1] = (numbers[i], -1, i)
            events[i] = (numbers[i + 1], 1, i)
        events = QuickSort(events).sort()
        return events

    def __check_segments(self, events, segment_count):
        good_segments = []
        current_segments = []
        is_good = True
        previous_time = -1

        for event in events:
            if event[0] != 0 and len(current_segments) == 0:
                is_good = False
                break
            if len(current_segments) == 1 and event[0] != previous_time:
                if current_segments[0] not in good_segments:
                    good_segments.append(current_segments[0])
            if event[1] == -1:
                current_segments.append(event[2])
            else:
                current_segments.remove(event[2])
            previous_time = event[0]

        if events[-1][0] != 10000:
            is_good = False

        return is_good and len(good_segments) == segment_count

    def run_tests(self):
        for test_idx, line in enumerate(self.test_lines):
            numbers = self.__parse_line(line)
            events = self.__process_events(numbers)
            if self.__check_segments(events, numbers[0]):
                self.results[test_idx] = "Accepted"
            else:
                self.results[test_idx] = "Wrong Answer"
        return "\n".join(self.results)


if __name__ == "__main__":

    # Запуск таймера.
    start_time = time.perf_counter()

    with open("input.txt", "r") as file:
        lines = file.readlines()
        test_count = int(lines[0])

    print(lines[1:])
    checker = SecurityTestChecker(test_count, lines[1:])
    result = checker.run_tests()

    with open("output.txt", "w") as file:
        file.write(result)

    stop_time = time.perf_counter()

    # Вывод времени выполнения.
    print("=" * 42)
    print(f"    Время выполнения: {stop_time - start_time:0.5f} секунд.")
    # Получение и вывод используемой памяти.
    final_memory = get_memory_usage()
    print(f"    Использовано памяти: {final_memory:.2f} Mb.")
    print("=" * 42)
