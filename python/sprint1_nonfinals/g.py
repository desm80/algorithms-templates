def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


def read_input() -> int:
    return int(input().strip())

# print(to_binary(5))
print(to_binary(read_input()))
