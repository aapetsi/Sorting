# TO-DO: Complete the selection_sort() function below
import random


def check_sorted(arr):
    for index, num in enumerate(arr):
        if index != len(arr) - 1:
            if arr[index] > arr[(index + 1)]:
                return False
    return True


def selection_sort(arr):
    arr_cp = arr[:]
    if len(arr_cp) <= 1:
        return arr_cp
    is_sorted = check_sorted(arr_cp)
    ret = []
    while len(arr_cp) != 0:
        for idx, val in enumerate(arr_cp):
            min_val = min(arr_cp[0:])
            min_index = arr_cp.index(min_val)
            ret.append(min_val)
            arr_cp.pop(min_index)
        is_sorted = check_sorted(arr_cp)
    return ret

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    is_sorted = check_sorted(arr)
    while not is_sorted:
        for index, num in enumerate(arr):
            if index != len(arr) - 1:
                first = num
                second = arr[index + 1]
                if first > second:
                    arr[index] = second
                    arr[index + 1] = first
        is_sorted = check_sorted(arr)
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
