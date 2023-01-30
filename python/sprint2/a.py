from typing import List


def transponse_matrix(matrix: List[List[int]]) -> List[List[int]]:
    matrix = zip(*matrix)
    return [list(row) for row in matrix]


def read_input() -> List[List[int]]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return matrix


# matrix = [
#     [1, 2, 3, 0],
#     [4, 5, 6, 1],
#     [7, 8, 9, 5],
# ]


if __name__ == '__main__':
    matrix = read_input()
    [print(*row) for row in transponse_matrix(matrix)]
