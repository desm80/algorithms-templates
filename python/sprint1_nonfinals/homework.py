# ID 81032442
from typing import List


def get_result(numbers: List[int],
               start: int,
               stop: int,
               step: int) -> List[int]:
    """Получение промежуточных списков расстояний до пустого участка."""
    result = []
    counter = 10 ** 6
    for i in range(start, stop, step):
        if numbers[i] == 0:
            result.append(0)
            counter = 0
        else:
            counter += 1
            result.append(counter)
    return result


def get_distance(numbers: List[int]) -> List[int]:
    """Сложение разнонаправленных списков для получения итогового расстояния
    до пустых участков."""
    get_straight = get_result(numbers, 0, len(numbers), 1)
    get_backwards = get_result(numbers, -1, -(len(numbers) + 1), -1)
    return [min(item) for item in zip(get_straight, get_backwards[::-1])]


def read_input() -> List[int]:
    """Чтение ввода со списком участков."""
    n = int(input())
    return [int(i) for i in input().strip().split()]


if __name__ == '__main__':
    numbers = read_input()
    print(*get_distance(numbers))
