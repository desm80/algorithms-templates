def get_longest_word(line: str) -> str:
    # b = sorted(a, key=len).pop()
    result = ''
    for word in line.split(' '):
        if len(word) > len(result):
            result = word
    return result

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))

# line = 'i love segment tree'
# a = line.split(' ')
# b = sorted(a, key=len).pop()
#
#
# print(b)