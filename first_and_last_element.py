def search_range(nums, target):
    first = find_first(nums, target)

    if first != -1:
        last = find_last(nums, target, first)
    else:
        last = -1

    return first, last

def find_first(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            if nums[mid] == target: index = mid
            right = mid - 1
        else:
            left = mid + 1

    return index


def find_last(nums, target, first):
    left, right = first, len(nums) - 1
    index = first

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            if nums[mid] == target: index = mid
            left = mid + 1
        else:
            right = mid - 1

    return index


if __name__ == '__main__':
    print(search_range([1, 2, 3, 4, 4, 5], 4))