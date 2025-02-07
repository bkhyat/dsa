def get_indices(array, target):
    left, right = 0, len(array) - 1

    while left<right:
        sum_ = array[left] + array[right]
        if sum_==target: return left, right
        elif sum_>target:
            right -= 1
        else:
            left += 1

if __name__ == "__main__":
    print(get_indices([2, 7, 11, 15], 9))