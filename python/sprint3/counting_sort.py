def counting_sort(array, k=3):
    counted_values = [0] * k
    for value in array:
        counted_values[int(value)] += 1

    pink = [0] * counted_values[0]
    yellow = [1] * counted_values[1]
    red = [2] * counted_values[2]


    # index = 0
    # for value in range(k):
    #     for amount in range(counted_values[value]):
    #         array[index] = value
    #         index += 1

    print(*(pink + yellow + red))

counting_sort(list('0 2 1 2 0 0 1'.split(' ')))
