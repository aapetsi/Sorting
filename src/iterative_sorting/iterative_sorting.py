# TO-DO: Complete the selection_sort() function below
import random


def check_sorted(arr):
    for index, num in enumerate(arr):
        if index != len(arr) - 1:
            if arr[index] > arr[(index + 1)]:
                return False
    return True


def selection_sort(arr):
    if len(arr) <= 1:
        return arr
    is_sorted = check_sorted(arr)
    ret = []
    while len(arr) != 0:
        for idx, val in enumerate(arr):
            min_val = min(arr[0:])
            min_index = arr.index(min_val)
            ret.append(min_val)
            arr.pop(min_index)
        is_sorted = check_sorted(arr)
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
