# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for index, val in arr:
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
    found = False
    while middle != len(arr) - 1:
      print(middle)
      if target > arr[middle]:
        low = middle + 1
        middle = (low + high) // 2
      elif target < arr[middle]:
        high = middle - 1
        middle = (low + high) // 2
      elif target == arr[middle]:
        target = arr[middle]
      #   found = True
      # else:
      #   found = True

    if target == arr[middle]:
      return middle  # not found
    else:
      return -1

print(binary_search([2,5,8,12,16,23,38,56,72,91], 913))

# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
