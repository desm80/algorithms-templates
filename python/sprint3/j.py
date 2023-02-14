from typing import List


def solution(n, numbers) -> None:
    f = True
    for i in range(n-1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                buff = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = buff
                f = True
        if f:
            print(*numbers)
            f = False


# def read_input() -> List[int]:
#     n = int(input())
#     return list(map(int, input().strip().split()))


if __name__ == '__main__':
    n = int(input())
    array = [int(num) for num in input().strip().split(' ')]
    # array = list(map(int, input().strip().split(' ')))
    solution(n, array)
