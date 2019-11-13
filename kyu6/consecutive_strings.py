from typing import List


def longest_consec(arr: List[str], k: int) -> str:
    arr_len = len(arr)
    if arr_len == 0 or k > arr_len or k <= 0:
        return ''
    slices = [arr[i:i+k] for i in range(0, arr_len - k + 1)]
    max_slice = max(slices, key=lambda strs: sum(len(s) for s in strs))
    return ''.join(max_slice)


assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == 'abigailtheta'
