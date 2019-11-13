# https://www.codewars.com/kata/integers-recreation-one/train/python
import test
from test import timed

import math
from typing import List, Set


def divisors(n: int) -> Set[int]:
    divs = set()
    # The secret sauce of this whole algorithm is the sqrt bound-setting below. Without this, running from (1, 30000)
    # takes around 23s. With this, it takes less than 1s!
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return divs


@timed
def list_squared(m: int, n: int) -> List[List[int]]:
    pairs = []
    for i in range(m, n + 1):
        divs = divisors(i)
        sum_sq = sum(x ** 2 for x in divs)
        sqrt = math.sqrt(sum_sq)
        if sqrt.is_integer():
            pairs.append([i, sum_sq])
    return pairs


test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
test.assert_equals(list_squared(250, 500), [[287, 84100]])
test.assert_equals(list_squared(1, 30000),
                   [[1, 1], [42, 2500], [246, 84100], [287, 84100], [728, 722500], [1434, 2856100], [1673, 2856100],
                    [1880, 4884100], [4264, 24304900], [6237, 45024100], [9799, 96079204], [9855, 113635600],
                    [18330, 488410000], [21352, 607622500], [21385, 488410000], [24856, 825412900]])
