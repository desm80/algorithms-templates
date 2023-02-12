# 81891701
from typing import List


class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_n = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """Проверка очереди на наличие элементов."""
        return self.size == 0

    def push_back(self, value):
        """Добавление элемента в конец очереди."""
        if self.size != self.max_n:
            if self.queue[self.tail]:
                self.tail = (self.tail + 1) % self.max_n
            self.queue[self.tail] = value
            self.size += 1
        else:
            raise Exception

    def push_front(self, value):
        """Добавление элемента в начало очереди."""
        if self.size != self.max_n:
            if self.queue[self.head]:
                self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = value
            self.size += 1
        else:
            raise Exception

    def pop_front(self):
        """Получение первого элемента очереди."""
        if self.is_empty():
            raise Exception
        x = self.queue[self.head]
        self.queue[self.head] = None
        if self.size > 1:
            self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        """Получение последнего элемента очереди."""
        if self.is_empty():
            raise Exception
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.size > 1:
            self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


def solution(commands, max_size):
    """Выполнение команд из списка и вывод результата, при наличии."""
    queue = Deque(max_size)
    for row in commands:
        try:
            res = getattr(queue, row.pop(0))(*row)
            if res:
                print(res)
        except:
            print('error')


def read_input() -> [List[List[str]]]:
    """Чтение списка команд и максимального значения очереди."""
    n = int(input())
    m = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands, m


if __name__ == '__main__':
    commands, max_size = read_input()
    solution(commands, max_size)
