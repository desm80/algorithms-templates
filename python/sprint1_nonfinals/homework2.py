# ID 81034098
from typing import Tuple


def get_points(number_list: str, k: int) -> int:
    """Подсчет баллов для игрового поля исходя из количества клавиш,
    доступных для нажимания."""
    counter = 0
    for i in range(10):
        if str(i) in number_list:
            if number_list.count(str(i)) <= 2 * k:
                counter += 1
    return counter


def read_input() -> Tuple[str, int]:
    """Чтение ввода со списком строк игрового поля и
    максимального количества клавиш для каждого игрока."""
    k = int(input())
    training = ''.join([input() for i in range(4)])
    return training, k


if __name__ == '__main__':
    training, k = read_input()
    print(get_points(training, k))
