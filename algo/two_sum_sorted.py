# Using two pointer
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[left] + arr[mid] == target:
            return [left, mid]
        elif arr[left] + arr[mid] < target:
            right -= 1
        else:
            left += 1

    return None


# using binary search
def two_sum_sorted_bs(arr, target):

    for index, value in enumerate(arr):

        target_number = target - value
        left, right = index + 1, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if target_number == arr[mid]:
                return [index, mid]
            elif target_number < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return None


if __name__ == "__main__":
    arr = [2, 7, 12, 15, 25]
    target = 17
    result = two_sum_sorted_bs(arr, target)
    print(result)
