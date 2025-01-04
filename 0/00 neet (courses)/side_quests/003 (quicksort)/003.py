def swap(idx_one, idx_two, arr):
    if idx_one == idx_two: return

    temp = arr[idx_one]
    arr[idx_one] = arr[idx_two]
    arr[idx_two] = temp


def explore_pivot_swaps(start, end, arr):
    if start >= end: return

    pivot = arr[end]

    idx = start
    insertion_point = start
    while idx < end:
        num = arr[idx]
        if num <= pivot:
            swap(idx, insertion_point, arr)
            insertion_point += 1
        idx += 1

    swap(insertion_point, end, arr)
    explore_pivot_swaps(start, insertion_point-1, arr)
    explore_pivot_swaps(insertion_point + 1, end, arr)

def quick_sort(arr):
    explore_pivot_swaps(0, len(arr) - 1, arr)

    return arr

a = [6, 2, 4, 1, 3]
quick_sort(a)
print(a)