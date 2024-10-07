from typing import List, Tuple
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


def read_file(filename: str) -> Tuple[int, List[List[Tuple[int, int]]]]:
    """Чтение данных из файла."""
    with open(filename, "r") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)

    lines = cleaned_lines

    num_records = int(lines[0])  # Первая строка содержит количество записей.

    time_intervals = lines[1:]  # Остальные строки содержат пары временных интервалов.

    intervals = []
    for interval in time_intervals:
        split_interval = interval.split()
        time_pairs = []
        for time_l in split_interval:
            time_parts = time_l.split(':')
            hours = int(time_parts[0])
            minutes = int(time_parts[1])
            time_pairs.append((hours, minutes))
        intervals.append(time_pairs)

    return num_records, intervals


class MuseumVisitors:
    def __init__(self, intervals: List[List[Tuple[int, int]]]) -> None:
        self.intervals = intervals

    def __quick_sort(self, events: List[Tuple[Tuple[int, int], str]], low: int, high: int) -> None:
        if low < high:
            mid = self.__partition(events, low, high)
            self.__quick_sort(events, low, mid - 1)
            self.__quick_sort(events, mid + 1, high)

    def __partition(self, events: List[Tuple[Tuple[int, int], str]], low: int, high: int) -> int:
        pivot = events[high][0]
        i = low - 1
        for j in range(low, high):
            if events[j][0] < pivot or (events[j][0] == pivot and events[j][1] == "enter"):
                i += 1
                events[i], events[j] = events[j], events[i]
        events[i + 1], events[high] = events[high], events[i + 1]
        return i + 1

    def find_max_visitors(self) -> int:
        events = []

        # Создаем события входа и выхода.
        for interval in self.intervals:
            start_time = interval[0]
            end_time = interval[1]
            events.append((start_time, "enter"))
            events.append((end_time, "exit"))

        # Сортируем события по времени, а затем по типу события (enter перед exit)
        self.__quick_sort(events, 0, len(events) - 1)

        max_visitors = 0
        current_visitors = 0

        # Проходим по отсортированным событиям
        for event in events:
            if event[1] == "enter":
                current_visitors += 1
                if current_visitors > max_visitors:
                    max_visitors = current_visitors
            elif event[1] == "exit":
                current_visitors -= 1

        return max_visitors


def main() -> None:
    # Запуск таймера.
    start_time = time.perf_counter()

    filename = "input.txt"
    num_records, intervals = read_file(filename)

    for interval in intervals:
        print(interval)

    museum = MuseumVisitors(intervals)
    max_visitors = museum.find_max_visitors()
    print(max_visitors)

    with open("output.txt", "w") as file:
        file.write(str(max_visitors))

    stop_time = time.perf_counter()

    # Вывод времени выполнения.
    print("=" * 42)
    print(f"    Время выполнения: {stop_time - start_time:0.5f} секунд.")
    # Получение и вывод используемой памяти.
    final_memory = get_memory_usage()
    print(f"    Использовано памяти: {final_memory:.2f} Mb.")
    print("=" * 42)


if __name__ == "__main__":
    main()