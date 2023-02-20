LIST_OF_STRINGS = []
PATTERN = {
    '(': ')',
}
RESULT_LIST = []


def gen_binary(n, prefix):
    if n == 0:
        LIST_OF_STRINGS.append(prefix)
    else:
        gen_binary(n - 1, prefix + '(')
        gen_binary(n - 1, prefix + ')')


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


if __name__ == "__main__":
    n = int(input())
    gen_binary(n * 2, '')
    for string in LIST_OF_STRINGS:
        if solution(string):
            RESULT_LIST.append(string)

    [print(string) for string in RESULT_LIST]
