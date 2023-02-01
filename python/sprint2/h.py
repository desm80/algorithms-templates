from typing import List

PATTERN = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []


def solution(string) -> bool:
    stack = Stack()
    for item in string:
        if item in PATTERN.keys():
            stack.push(item)
        elif not stack.isEmpty() and PATTERN.get(stack.peek()) == item:
            stack.pop()
        else:
            stack.push(item)
    if stack.isEmpty():
        return True
    return False


def read_input() -> List[str]:
    return list(input())


if __name__ == '__main__':
    string = read_input()
    print(solution(string))
