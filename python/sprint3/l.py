

def binarySearch(arr, x, left, right) -> int:
    if right <= left and left !=0:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and (arr[mid-1] < x or mid == 0):
        return mid + 1
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def solution():
    pass


def read_input():
    right = int(input())
    arr = [int(num) for num in input().strip().split()]
    s = int(input())
    return arr, s


if __name__ == '__main__':
    arr, s = read_input()
    # s = 3
    # arr = [1, 2, 4, 4, 6, 8]
    index_1 = binarySearch(arr, s, 0, len(arr))
    index_2 = binarySearch(arr, s * 2, 0, len(arr))
    print(index_1, index_2)
