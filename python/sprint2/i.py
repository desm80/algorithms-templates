from typing import List


class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
           return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def solution(commands, max_size) -> None:
    queue = MyQueueSized(max_size)
    for row in commands:
        if len(row) == 0 or len(row) >= 3:
            continue
        if len(row) == 2:
            queue.push(int(row[1]))
        if len(row) == 1 and row[0] == 'pop':
            print(queue.pop())
        if len(row) == 1 and row[0] == 'peek':
            print(queue.peek())
        if len(row) == 1 and row[0] == 'size':
            print(queue.size)


def read_input() -> [List[List[str]]]:
    n = int(input())
    max_size = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands, max_size


if __name__ == '__main__':
    commands, max_size = read_input()
    solution(commands, max_size)


# q = Queue(8)
# q.push(1)
# print(q.queue)  # [1, None, None, None, None, None, None, None]
# print(q.size)   # 1
# q.push(-1)
# q.push(0)
# q.push(11)
# print(q.queue)  # [1, -1, 0, 11, None, None, None, None]
# print(q.size)   # 4
#
# q.pop()
# print(q.queue)  # [None, -1, 0, 11, None, None, None, None]
# print(q.size)   # 3
#
# q.pop()
# q.pop()
# q.push(-8)
# q.push(7)
# q.push(3)
# q.push(16)
# print(q.queue) # [None, None, None, 11, -8, 7, 3, 16]
# print(q.size) # 5
# q.push(12)
# print(q.queue) # [12, None, None, 11, -8, 7, 3, 16]
# print(q.size) # 6