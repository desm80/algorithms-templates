from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    # if len(first_number) >= len(second_number):
    #     digit = len(first_number)
    # else:
    #     digit = len(second_number)

    digit = max(len(first_number), len(second_number))

    a = len(first_number) - len(second_number)
    if a > 0:
        second_number = '0' * abs(a) + second_number
    else:
        first_number = '0' * abs(a) + first_number

    result = ''
    in_mind = 0

    for i in range(-1, -(digit) - 1, -1):
        sum = int(first_number[i]) + int(second_number[i]) + in_mind
        if sum == 0:
            result = '0' + result
            in_mind = 0
        if sum == 1:
            result = '1' + result
            in_mind = 0
        if sum == 2:
            result = '0' + result
            in_mind = 1
        if sum == 3:
            result = '1' + result
            in_mind = 1
    if in_mind == 0:
        return result
    return '1' + result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


# first_number, second_number = read_input()
# print(get_sum(first_number, second_number))
print(get_sum('11111', '1111'))
