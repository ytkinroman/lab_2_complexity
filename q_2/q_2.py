from typing import List, Tuple
import time
import os
import psutil


def get_memory_usage():
    """Получение используемой памяти в мегабайтах."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


class Participant:
    def __init__(self, login: str, solved: int, penalty: int):
        """Инициализация участника."""
        self.login = login
        self.solved = solved
        self.penalty = penalty

    def __lt__(self, other):
        """Метод сравнения участников для сортировки."""
        # Сравнение по количеству решенных задач
        if self.solved != other.solved:
            return self.solved > other.solved

        # Сравнение по штрафу
        if self.penalty != other.penalty:
            return self.penalty < other.penalty

        # Сравнение по логину
        return self.login < other.login


class QuickSort:
    def __init__(self, participants: List[Participant]) -> None:
        """Инициализация быстрой сортировки."""
        self.participants = participants

    def __quick_sort(self, low: int, high: int) -> None:
        """Алгоритм быстрой сортировки."""
        if low < high:
            # Разделение массива
            mid = self.__partition(low, high)
            # Рекурсивная сортировка левой части
            self.__quick_sort(low, mid - 1)
            # Рекурсивная сортировка правой части
            self.__quick_sort(mid + 1, high)

    def __partition(self, low: int, high: int) -> int:
        """Функция разделения массива."""
        # Выбор опорного элемента
        pivot = self.participants[high]
        i = low - 1
        for j in range(low, high):
            # Сравнение элементов с опорным
            if self.participants[j] < pivot:  # (__lt__)
                i += 1
                # Обмен элементов
                self.participants[i], self.participants[j] = self.participants[j], self.participants[i]
        # Обмен опорного элемента
        self.participants[i + 1], self.participants[high] = self.participants[high], self.participants[i + 1]
        return i + 1

    def sort(self) -> List[Participant]:
        """Сортировка массива с помощью быстрой сортировки."""
        # Запуск быстрой сортировки
        self.__quick_sort(0, len(self.participants) - 1)
        return self.participants


def main():
    # Чтение количества участников
    n = int(input())

    participants = []
    for _ in range(n):
        # Чтение данных участника
        input_login,  input_solved,  input_penalty = input().split()
        input_solved = int(input_solved)
        input_penalty = int(input_penalty)
        # Добавление участника в список
        participants.append(Participant(input_login,  input_solved,  input_penalty))

    # Запуск таймера
    start_time = time.perf_counter()

    # Сортировка участников
    sorter = QuickSort(participants)
    sorted_participants = sorter.sort()

    # Вывод отсортированных логинов
    for participant in sorted_participants:
        print(participant.login)

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
