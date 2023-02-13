PATTERN ={
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


# def gen_binary(n, prefix):
#     if n == 0:
#        print(prefix)
#     else:
#         for letter in PATTERN.get(2):
#             gen_binary(n - 1, prefix + letter)
#
#
# # string = ['abc', ]
# for letter in PATTERN.get(9):
#     gen_binary(1, letter)

def gen_binary(string):
    n = len(string)-1
    if n == 0:
       print(prefix)
    else:
        for letter in PATTERN.get(2):
            gen_binary(n - 1, prefix + letter)





string = list(map(int, input()))
seqs = []
for number in string:
    seqs.append(list(PATTERN[number]))

print(*seqs)
