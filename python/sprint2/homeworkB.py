# 81862039
from typing import List

OPERATORS = ['+', '-', '*', '/']


class Stack:
    def __init__(self):
        self.items = []
        self.result = []

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
        if item not in OPERATORS:
            stack.push(item)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if item == '+':
                stack.push(str(int(a + b)))
            if item == '-':
                stack.push(str(int(a - b)))
            if item == '/':
                stack.push(str(int(a // b)))
            if item == '*':
                stack.push(str(int(a * b)))
    return int(stack.pop())


def read_input() -> List[str]:
    """Чтение ввода строки с обратной польской нотацией."""
    return list(input().strip().split())


if __name__ == '__main__':
    string = read_input()
    print(solution(string))
