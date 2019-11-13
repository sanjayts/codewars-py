from typing import List


def find_even_index(arr: List[int]) -> int:
    arr_sz = len(arr)
    for i in range(arr_sz):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
