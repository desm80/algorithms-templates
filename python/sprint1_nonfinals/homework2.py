# ID 80972427
from typing import List, Tuple


def get_points(number_list: List[str], k: int) -> int:
    """Подсчет баллов для игрового поля исходя из количества клавиш,
    доступных для нажимания."""
    result = []
    counter = 0
    for string in number_list:
        result.append(list(string))
    final_string = sum(result, [])
    for i in range(10):
        if str(i) in final_string:
            if final_string.count(str(i)) <= 2 * k:
                counter += 1
    return counter


def read_input() -> Tuple[List[str], int]:
    """Чтение ввода со списком строк игрового поля и
    максимального количества клавиш для каждого игрока."""
    k = int(input())
    training = []
    for i in range(4):
        numbers = input()
        training += numbers
    return training, k


if __name__ == '__main__':
    training, k = read_input()
    print(get_points(training, k))

# print(get_points(['1231', '2..2', '2..2', '2..2'], 3))
