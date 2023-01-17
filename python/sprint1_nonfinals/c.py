from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []

    for i in range(col - 1, col + 2, 2):
        if i >= 0 and i <= len(matrix[row]) - 1:
            result.append(matrix[row][i])
    for i in range(row - 1, row + 2, 2):
        if i >= 0 and i <= len(matrix) - 1:
            result.append(matrix[i][col])

    result.sort()
    return result

# def read_input() -> Tuple[List[List[int]], int, int]:
#     n = int(input())
#     # m = int(input())
#     matrix = []
#     for i in range(n):
#         matrix.append(list(map(int, input().strip().split())))
#     row = int(input())
#     col = int(input())
#     return matrix, row, col
#
# matrix, row, col = read_input()
# print(" ".join(map(str, get_neighbours(matrix, row, col))))

matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 1],
    [7, 8, 9, 5],
]
row = 2
col = 0
# print(len(matrix))

print(" ".join(map(str, get_neighbours(matrix, row, col))))
