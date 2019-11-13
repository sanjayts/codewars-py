import functools
from typing import List


def find_it(seq: List[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, seq[1:], seq[0])
