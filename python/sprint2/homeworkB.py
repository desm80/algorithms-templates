# 81891535
from typing import List

OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавление элемента в стэк."""
        self.items.append(item)

    def pop(self):
        """Получение элемента из стэка."""
        return self.items.pop()


def solution(string) -> int:
    """Выполнение арифметических операций согласно полученным данным."""
    stack = Stack()
    for item in string:
        if item not in OPERATORS.keys():
            stack.push(item)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            stack.push(str((OPERATORS.get(item)(a, b))))
    return int(stack.pop())


def read_input() -> List[str]:
    """Чтение ввода строки с обратной польской нотацией."""
    return list(input().strip().split())


if __name__ == '__main__':
    string = read_input()
    print(solution(string))
