

# a = [0,1,2,3,4,5,6,7,8]
# print(a[::-1])
# print(list(reversed(a)))
#
# matrix = [
#     [1, 2, 3, 0],
#     [4, 5, 6, 1],
#     [7, 8, 9, 5],
# ]
#
# c = sum(matrix, [])
# print(c)

a = ['1234', '..34', '98.2', '23.1', ]
result = []
for string in a:
   result.append(list(string))
result2 = sum(result, [])
i = result2.count('2')

print(result2)
print(i)




