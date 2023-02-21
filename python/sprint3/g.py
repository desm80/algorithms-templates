
def solution(string):
    pink = ''
    yellow = ''
    red = ''
    for i in string:
        if i == '0':
            pink += i
        elif i == '1':
            yellow += i
        else:
            red += i
    print(*list(pink + yellow + red))


if __name__ == '__main__':
    _ = input()
    string = list(input().split(' '))
    solution(string)


# def solution(string):
#     pink = ''
#     yellow = ''
#     red = ''
#     for i in range(len(string)):
#         if string[i] == '0':
#             pink += string[i]
#         elif string[i] == '1':
#             yellow += string[i]
#         else:
#             red += string[i]
#     return pink + yellow + red
#
#
# if __name__ == '__main__':
#     input()
#     string = ''.join([''.join(index) for index in input().strip().split()])
#     print(' '.join([''.join(index) for index in solution(string)]))
