from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    return sum(map(list, zip(a, b)), [])


def read_input() -> Tuple[List[int], List[int]]:

    n = int(input('n>'))
    a = list(map(int, input('a>').strip().split()))
    b = list(map(int, input('b>').strip().split()))
    if len(a) != n or len(b) != n:
        raise Exception("Длина списков не одинакова или не соответствует n")
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
