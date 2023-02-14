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


# def gen_binary(string):
#     if string == '':
#         return ['']
#
#     result = []
#     word = PATTERN[string[-1]]
#     for comb in gen_binary(string[:-1:]):
#         for c in word:
#             result.append(comb + c)
#     return result
#
# string = input()
# print(' '.join(gen_binary(string)))


def create_all_pairs(*seqs):
    if not seqs:
        return [[]]
    else:
        return [[x] + p for x in seqs[0] for p in create_all_pairs(*seqs[1:])]


numbers = list(map(int, input()))
seqs = []
for number in numbers:
    seqs.append(list(PATTERN[str(number)]))
result = create_all_pairs(*seqs)
print(' '.join([''.join(index) for index in result]))

