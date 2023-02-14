# def insertion_sort(array):
#     for i in range(1, len(array)):
#         item_to_insert = array[i]
#         j = i
#         while j > 0 and item_to_insert < array[j - 1]:
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = item_to_insert
#         # print(f'step {i}, sorted {i+1} elements: {array}')
#     print(array)
#
# insertion_sort([11, 2, 2, 9, 7, 1])

a = '4 3 9 2 1'
print(list(map(int, a.strip().split())))