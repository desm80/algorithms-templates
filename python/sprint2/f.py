from typing import List


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        return max(self.items)


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
