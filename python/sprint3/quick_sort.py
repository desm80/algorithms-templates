import random


# def partition(nums, low, high):
# """Сортировка Хоара без использования дополнительной памяти."""
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quick_sort(nums):
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
#
#
# # Проверяем, что оно работает
# random_list_of_nums = [22, 5, 1, 5, 10, 5, 78, 5, 18, 99]
# quick_sort(random_list_of_nums)
# print(random_list_of_nums)


def partition(array, pivot):
    # left = [i for i in array if i < pivot] #элементы array, меньшие pivot
    # center = [i for i in array if i == pivot] #элементы array, равные pivot
    # right = [i for i in array if i > pivot] #элементы array, большие pivot
    left = []
    center = []
    right = []
    for number in array:
        if number < pivot:
            left.append(number)
        elif number > pivot:
            right.append(number)
        else:
            center.append(number)
    return left, center, right


def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[random.randint(0, len(array) - 1)]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


random_list_of_nums = [22, 5, 1, 5, 10, 5, 78, 5, 18, 99]
quicksort(random_list_of_nums)
print(quicksort(random_list_of_nums))
