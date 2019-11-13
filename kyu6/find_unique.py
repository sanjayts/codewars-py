from collections import Counter
from typing import List, Union


# An efficient solution which iterates the array only once and does an early exit if the criteria is met
# O(1) -- constant space complexity
# O(n) -- time complexity but faster in practice compared to the below solution due to early exits and no
# mandatory full list traversal requirement
def find_uniq(arr: List[Union[int, float]]) -> Union[int, float]:
    v1, v2 = arr[0], None
    for idx, v in enumerate(arr[1:]):
        if v != v1:
            if v2 is None:
                v2 = v
            else:
                return v1
        else:
            if v2 is not None:
                return v2
    return arr[-1]


def find_uniq_concise(arr: List[Union[int, float]]) -> Union[int, float]:
    a, b = set(arr)
    c = Counter(arr[:3])  # Notice that we pick up only the first 3 elements
    uniq = a if c.most_common(1)[0][0] == a else b
    return uniq


out = find_uniq([2, 1, 1, 1, 1, 1, 1])
print(out)
