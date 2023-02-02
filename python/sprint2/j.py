from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.head != self.tail:
            # Has at least two elements
            res = self.head
            self.head = self.head.next
            self.size -= 1
            return res
            # Has one or zero element
        res = self.head
        self.head = None
        self.tail = None
        self.size -= 1
        return res

    def put(self, x):
        node = Node(x)
        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def size(self):
        return self.size

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        try:
            temp = self.cur
            self.cur = self.cur.next
            return temp
        except AttributeError as e:
            raise StopIteration


def solution(commands):
    queue = Queue()
    for row in commands:
        if len(row) == 0 or len(row) >= 3:
            continue
        if len(row) == 2:
            queue.put(int(row[1]))
        if len(row) == 1 and row[0] == 'get':
            print(queue.get().item)
        if len(row) == 1 and row[0] == 'size':
            print(queue.size)


def read_input() -> [List[List[str]]]:
    n = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
