from typing import List


class Participant:
    __slots__ = ['name', 'solved_tasks', 'penalty']

    def __init__(self, name: str, solved_tasks: int, penalty: int) -> None:
        self.name = name
        self.solved_tasks = solved_tasks
        self.penalty = penalty

    def __lt__(self, other: 'Participant') -> bool:
        if self.solved_tasks == other.solved_tasks:
            if self.penalty > other.penalty:
                return True
            elif self.penalty == other.penalty:
                return self.name > other.name
        return other.solved_tasks > self.solved_tasks

    def __str__(self) -> str:
        return self.name


def partition(participants, low, high) -> None:
    """Сортировка Хоара без использования дополнительной памяти."""
    pivot = participants[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while participants[i] < pivot:
            i += 1
        j -= 1
        while participants[j] > pivot:
            j -= 1
        if i >= j:
            return j
        participants[i], participants[j] = participants[j], participants[i]


def quick_sort(participants) -> None:
    """Рекурсивная функция для вызова быстрой сортировки."""
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(participants, low, split_index)
            _quick_sort(participants, split_index + 1, high)

    _quick_sort(participants, 0, len(participants) - 1)


def read_input() -> List[Participant]:
    """Чтение ввода данных."""
    n = int(input())
    participants = []
    for i in range(n):
        name, tasks, penalty = input().split()
        participants.append(Participant(name=name, solved_tasks=int(tasks),
                                        penalty=int(penalty)))
    return participants


if __name__ == '__main__':
    participants = read_input()
    quick_sort(participants)
    [print(i) for i in participants[::-1]]
