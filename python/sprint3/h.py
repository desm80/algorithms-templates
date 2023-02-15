# def gen_binary(string):
#     if string == '':
#         return ['']
#
#     result = []
#     word = string[-1]
#     for comb in gen_binary(string[:-1:]):
#         for c in word:
#             result.append(comb + c)
#     return result
#
# print

# def create_all_pairs(seqs):
#
#     if not seqs:
#         return []
#
#     return [x + p for x in seqs for p in create_all_pairs(seqs[1::])]

    # for x in seqs:
    #     for p in create_all_pairs(seqs[1::]):
    #          result.append(x+p)
    #
    # return result
        # return [x + p for x in seqs for p in create_all_pairs(seqs[1:])]


# numbers = list(map(str, input().strip().split()))
# seqs = []
# for number in numbers:
#     seqs.append(list(PATTERN[str(number)]))
# result = create_all_pairs(['15', '56', '2'])
# print(result)
# print(' '.join([''.join(index) for index in result]))

# def comparate(num1, num2):
#     return num1 < num2
#
#
# def insertion_sort(array, less):
#     for i in range(1, len(array)):
#         key_item = array[i]
#         j = i - 1
#         while j >= 0 and less(int(array[j] + key_item), int(key_item + array[j])):
#             array[j], array[j + 1] = array[j + 1], array[j]
#             j -= 1
#     print(''.join(array))
#
#
# if __name__ == '__main__':
#     number = int(input())
#     source_array = input().split(' ')
#     print(source_array)
#     insertion_sort(source_array, comparate)
#
#
def comparator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        var1 = number_1 + number_2
        var2 = number_2 + number_1
        return var1 > var2


def max_number_summator(numbers_arr, comparator):
    for i in range(1, len(numbers_arr)):
        item_to_insert = numbers_arr[i]
        j = i
        while j > 0 and comparator(item_to_insert, numbers_arr[j - 1]):
            numbers_arr[j] = numbers_arr[j - 1]
            j -= 1
            numbers_arr[j] = item_to_insert
    return numbers_arr


num = input('>')
numbers_arr = [x for x in input('>').split(' ')]
print(''.join(max_number_summator(numbers_arr, comparator)))
