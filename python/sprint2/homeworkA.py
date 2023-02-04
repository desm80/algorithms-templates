# 81809126
from typing import List


class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_n = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_n:
            if self.queue[self.tail]:
                self.tail = (self.tail + 1) % self.max_n
            self.queue[self.tail] = value
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size != self.max_n:
            if self.queue[self.head]:
                self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = value
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        if self.size > 1:
            self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.size > 1:
            self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


def solution(commands, max_size):
    queue = Deque(max_size)
    for row in commands:
        res = getattr(queue, row.pop(0))(*row)
        if res:
            print(res)


def read_input() -> [List[List[str]]]:
    n = int(input())
    m = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands, m


if __name__ == '__main__':
    commands, max_size = read_input()
    solution(commands, max_size)
