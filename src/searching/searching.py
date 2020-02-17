# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for index, val in enumerate(arr):
        if val == target:
            return index

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1
    middle = (low + high) // 2

    # TO-DO: add missing code
    for x in arr:
        # print(middle)
        if target > arr[middle]:
            low = middle + 1
            middle = (low + high) // 2
        elif target < arr[middle]:
            high = middle - 1
            middle = (low + high) // 2
        elif target == arr[middle]:
            target = arr[middle]
            return middle
        else:
            middle = -1

    if target == arr[middle]:
        return middle  # not found
    else:
        return -1


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1
    if (low == high):
        if (target == arr[low]):
            return low
        else:
            return -1
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low, mid - 1)
        elif target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, high)


def interpolation_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1
    middle = nearest_mid(arr, target, low, high)

    # TO-DO: add missing code
    for x in arr:
        # print(middle)
        if target > arr[middle]:
            low = middle + 1
            middle = (low + high) // 2
        elif target < arr[middle]:
            high = middle - 1
            middle = (low + high) // 2
        elif target == arr[middle]:
            target = arr[middle]
            return middle
        else:
            middle = -1

    if target == arr[middle]:
        return middle  # not found
    else:
        return -1


def nearest_mid(arr, target, low, high):
    return low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

