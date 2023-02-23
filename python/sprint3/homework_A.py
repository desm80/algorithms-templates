def broken_search(nums, target) -> int:
    # first = 0
    # last = len(nums) - 1
    # index = -1
    # while (first <= last) and (index == -1):
    #     mid = (first + last) // 2
    #     if nums[mid] == target:
    #         index = mid
    #     else:
    #         if target < nums[mid]:
    #             last = mid - 1
    #         else:
    #             first = mid + 1
    # return index
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return mid
        if nums[first] <= nums[mid]:
            if nums[first] <= target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        else:
            if nums[mid] < target <= nums[last]:
                first = mid + 1
            else:
                last = mid - 1
    else:
        return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    _ = input()
    target = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, target))
