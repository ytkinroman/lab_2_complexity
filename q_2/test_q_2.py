import unittest
from q_2 import Participant, QuickSort


class TestCase(unittest.TestCase):
    def test_sort_1(self):
        """1. Тестирование на сортировку."""
        n = 5

        participants = []
        participants.append(Participant("alla", 4, 100))
        participants.append(Participant("gena", 6, 1000))
        participants.append(Participant("gosha", 2, 90))
        participants.append(Participant("rita", 2, 90))
        participants.append(Participant("timofey", 4, 80))

        sorter = QuickSort(participants)
        sorted_participants = sorter.sort()

        participants_result = ["gena", "timofey", "alla", "gosha", "rita"]

        for i in range(len(participants_result)):
            self.assertEqual(sorted_participants[i].login, participants_result[i])

    def test_sort_2(self):
        """2. Тестирование на сортировку."""
        n = 5

        participants = []
        participants.append(Participant("alla", 0, 0))
        participants.append(Participant("gena", 0, 0))
        participants.append(Participant("gosha", 0, 0))
        participants.append(Participant("rita", 0, 0))
        participants.append(Participant("timofey", 0, 0))

        sorter = QuickSort(participants)
        sorted_participants = sorter.sort()

        participants_result = ["alla", "gena", "gosha", "rita", "timofey"]

        for i in range(len(participants_result)):
            self.assertEqual(sorted_participants[i].login, participants_result[i])
