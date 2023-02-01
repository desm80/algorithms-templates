from typing import List


class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.isEmpty() or item >= self.max[-1]:
            self.max.append(item)
        self.items.append(item)

    def pop(self):
        removed = self.items.pop()
        if removed == self.max[-1]:
            self.max.pop()
        if self.isEmpty():
            self.max.clear()
        return removed

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        return self.max[-1]


def solution(commands, stack) -> None:
    for row in commands:
        if len(row) == 0 or len(row) >= 3:
            continue
        if len(row) == 2:
            stack.push(int(row[1]))
        if len(row) == 1 and row[0] == 'get_max':
            if stack.size() != 0:
                print(stack.get_max())
                continue
            print('None')
        if len(row) == 1 and row[0] == 'pop':
            if stack.size() != 0:
                stack.pop()
                continue
            print('error')


def read_input() -> [List[List[str]]]:
    n = int(input())
    commands = []
    for i in range(n):
        commands.append(list(map(str, input().strip().split())))
    return commands


if __name__ == '__main__':
    commands = read_input()
    stack = Stack()
    solution(commands, stack)