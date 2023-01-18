from typing import List


def get_distance(numbers: List[int]) -> List[int]:
    result = []
    result2 = []
    counter = 10 ** 6
    for i in range(len(numbers)):
        if numbers[i] == 0:
            result.append(0)
            counter = 0
        else:
            counter += 1
            result.append(counter)

    counter = 10 ** 6
    for i in range(-1, -len(numbers) - 1, -1):
        if numbers[i] == 0:
            result2.append(0)
            counter = 0
        else:
            counter += 1
            result2.append(counter)

    # result3 = map(min, zip(result, reversed(result2)))
    result3 = map(min, zip(result, result2[::-1]))

    return result3


def read_input() -> List[int]:
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    return numbers


# numbers = read_input()
# print(" ".join(map(str, get_distance(numbers))))
print(" ".join(map(str, get_distance([1,2,3,0,4,5,6,7,78,0,34,35,56,0,22,
33]))))
