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
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n
            self.queue[self.head] = value
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            print('error')
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            print('error')
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x


def solution(commands, max_size):
    queue = Deque(max_size)
    for row in commands:
        if len(row) == 0 or len(row) >= 3:
            continue
        # if len(row) == 2:
        #     queue.push(int(row[1]))
        # if len(row) == 1 and row[0] == 'pop':
        #     print(queue.pop())
        # if len(row) == 1 and row[0] == 'peek':
        #     print(queue.peek())
        # if len(row) == 1 and row[0] == 'size':
        #     print(queue.size)


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
