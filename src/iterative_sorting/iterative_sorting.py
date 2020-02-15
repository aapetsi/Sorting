# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    is_sorted = sorted(arr)
    ret = []
    while len(arr) != 0:
        for idx, val in enumerate(arr):
            min_val = min(arr[0:])
            min_index = arr.index(min_val)
            ret.append(min_val)
            print(ret)
            print(arr)
            arr.pop(min_index)
            print(min_val, min_index)
            print(len(ret))
        is_sorted = sorted(arr)
    return ret



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    is_sorted = sorted(arr)
    while not is_sorted:
        for index, num in enumerate(arr):
            if index != len(arr) - 1:
                first = num
                second = arr[index + 1]
                if first > second:
                    arr[index] = second
                    arr[index + 1] = first
        is_sorted = sorted(arr)
    return arr

def sorted(arr):
    for index, num in enumerate(arr):
        if index != len(arr) - 1:
            if arr[index] > arr[(index + 1)]:
                return False
    return True

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr