# def insertion_sort(array):
#     for i in range(1, len(array)):
#         item_to_insert = array[i]
#         j = i
#         while j > 0 and item_to_insert < array[j - 1]:
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = item_to_insert
#         print(f'step {i}, sorted {i+1} elements: {array}')
#     print(array)
#
# insertion_sort([11, 2, 2, 9, 7, 1])

# a = '4 3 9 2 1'
# print(list(map(int, a.strip().split())))


# digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6] # длины слов «ноль», «один»,...
#
#
# def card_strength(card): # ключ сравнения
#     return digit_lengths[card]
#
#
# # воспользуемся уже знакомой сортировкой вставками
# def insertion_sort_by_key(array, key):
#     for i in range(1, len(array)):
#         item_to_insert = array[i]
#         j = i
#         # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
#         while j > 0 and key(item_to_insert) < key(array[j - 1]):
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = item_to_insert
#         print(f'step {i}, sorted {i + 1} elements: {array}')
#
#
# cards = [3, 7, 9, 2, 3]
# insertion_sort_by_key(cards, card_strength)


# digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...
#
#
# def is_first_card_weaker(card_1, card_2):  # функция-компаратор
#     return digit_lengths[card_1] < digit_lengths[card_2]
#
#
# # воспользуемся уже знакомой сортировкой вставками
# def insertion_sort_by_comparator(array, less):
#     for i in range(1, len(array)):
#         item_to_insert = array[i]
#         j = i
#         # заменим сравнение item_to_insert < array[j-1] на компаратор less
#         while j > 0 and less(item_to_insert, array[j - 1]):
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = item_to_insert
#         print(f'step {i}, sorted {i + 1} elements: {array}')
#
#
# cards = [3, 7, 9, 2, 3]
# insertion_sort_by_comparator(cards, is_first_card_weaker)



def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array
    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0:int(len(array)/2)])
    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[int(len(array)/2):len(array)])
    # заводим массив для результата сортировки
    result = [] * len(array)
    # сливаем результаты
    l, r = 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result.append(left[l])   # перенеси оставшиеся элементы left в result
        l += 1
    while r < len(right):
        result.append(right[r])  # перенеси оставшиеся элементы right в result
        r += 1
    return result


print(merge_sort([1,6,3,2,8,4]))
