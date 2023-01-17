# from typing import Tuple
#
#
# def get_sum(a: int, b: int) -> int:
#     # Здесь реализация вашего решения
#     pass
#
#
# def read_input() -> Tuple[int, int]:
#     a = int(input())
#     b = int(input())
#     return a, b
#
#
# a, b = read_input()
# print(get_sum(a, b))


# def eratosthenes(n):
#     numbers = list(range(n + 1))
#     numbers[0] = numbers[1] = False
#     for num in range(2, n):
#         if numbers[num]:
#             for j in range(2 * num, n + 1, num):
#                 numbers[j] = False
#     return numbers
#
#
# print(eratosthenes(9))
a = [
    [1,2,3],
    [4,5,6,6,7,8],
    [7,8,9]
]
print(len(a[1]))
