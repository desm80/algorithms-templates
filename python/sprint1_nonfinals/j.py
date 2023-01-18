from typing import List


def factorize(number: int) -> List[int]:
    i = 2
    result = []
    while i * i <= number:
        if number % i == 0:
            result.append(i)
            number //= i
        else:
            i += 1

    if number > 1:
        result.append(int(number))
    result.sort()
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))

