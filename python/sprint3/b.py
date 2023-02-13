PATTERN = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def gen_binary(string):
    if string == '':
        return ['']

    result = []
    word = PATTERN[string[-1]]
    for comb in gen_binary(string[:-1:]):
        print(comb)
        for c in word:
            print(c)
            result.append(comb + c)
    return result

string = input()
print(' '.join(gen_binary(string)))





# def combinations(input_string):
#     d = {'2': 'abc',
#          '3': 'def',
#          '4': 'ghi',
#          '5': 'jkl',
#          '6': 'mno',
#          '7': 'pqrs',
#          '8': 'tuv',
#          '9': 'wxyz'}
#
#     if input_string == '':
#         return ['']
#
#     data = []
#     word = d[input_string[-1]]
#
#     for combination in combinations(input_string[:-1:]):
#         for c in word:
#             data.append(combination + c)
#
#     return data
#
#
# print(' '.join(combinations(input())))