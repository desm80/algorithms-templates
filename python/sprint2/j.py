from typing import List


class Queue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.qsize = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.qsize == 1:
            removed = self.head
            self.__init__()
            return removed.value
        if self.qsize == 2:
            removed = self.head
            self.head = self.tail
            self.qsize -= 1
            return removed.value
        removed = self.head
        self.head = self.tail.next_item.next_item
        self.tail.next_item = self.head
        self.qsize -= 1
        return removed.value

    def put(self, x):
        if self.is_empty():
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next_item = self.Node(value=x)
            self.tail.next_item.next_item = self.head
            self.tail = self.tail.next_item
        self.qsize += 1

    def size(self):
        return self.qsize

    # def __iter__(self):
    #     self.cur = self.head
    #     return self
    #
    # def __next__(self):
    #     try:
    #         temp = self.cur
    #         self.cur = self.cur.next
    #         return temp
    #     except AttributeError as e:
    #         raise StopIteration


def solution(commands):
    queue = Queue()
    for row in commands:
        if len(row) == 0 or len(row) >= 3:
            continue
        if len(row) == 2:
            queue.put(int(row[1]))
        if len(row) == 1 and row[0] == 'get':
            print(queue.get())
        if len(row) == 1 and row[0] == 'size':
            print(queue.size())


def read_input() -> [List[List[str]]]:
    n = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
