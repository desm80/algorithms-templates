def solution(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    index_str1 = 0
    index_str2 = 0
    while index_str1 < len_str1 and index_str2 < len_str2:
        if str1[index_str1] == str2[index_str2]:
            index_str1 += 1
        index_str2 += 1
    return index_str1 == len_str1


def read_input():
    str1 = str(input())
    str2 = str(input())
    return str1, str2


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(solution(str1, str2))
