# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if b[j] >= a[i]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < len(a):
        res.append(a[i])
        i += 1

    while j < len(b):
        res.append(b[j])
        j += 1

    return res


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])

    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
