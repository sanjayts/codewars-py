# https://www.codewars.com/kata/sum-of-pairs/train/python

from typing import List, Optional
import test


def sum_pairs(ints: List[int], s: int) -> Optional[List[int]]:
    pairs = []
    seen = set()
    for i, fst in enumerate(ints):
        # The first and most important step of optimization -- this is to ensure we skip pathological cases wherein the
        # same number gets repeated loads of times (think millions). Of course, this doesn't save us from the most
        # extreme case wherein we have an array of unique million elements resulting in a linear scan every time.
        if fst in seen:
            continue
        seen.add(fst)

        # The next optimization, though not as important as the previous one, this cuts down the
        # execution time by almost 40% (8.9s v/s 5.3s). Here we ensure that if we have already found the ideal match,
        # we break out early, instead of continuing with our loop. Let's say you are iterating over a million element
        # list and the pair we are interested in shows up at location (0, 1). It would be useless to discover other
        # candidate solutions only to throw them away later!
        if pairs:
            latest = pairs[-1]
            if i >= latest[1]:
                break

        # The third step in optimization -- instead of adding the current element with pivot element and then comparing
        # it with the expected outcome, let's just compute the diff and search for it. Sure, it's a linear search but
        # it at least alleviates us from doing an extra addition
        diff = s - fst
        try:
            j = ints.index(diff, i + 1)
            pairs.append([i, j])
        except ValueError:
            pass

    if pairs:
        i, j = min(pairs, key=lambda p: p[1])
        return [ints[i], ints[j]]
    else:
        return None


# Of all the solutions submitted to codewars, the below one was the most efficient, concise and oh-so-simple when you
# get it; hats off to the author :)
def sum_pairs_efficient(ints: List[int], s: int) -> Optional[List[int]]:
    seen = set()
    for i in ints:
        if (s - i) in seen:
            return [s - i, i]
        seen.add(i)
    return None


l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]
l9 = [1, 1, 1, 1, 1, 1, 1, 1, 1]

for func in [sum_pairs, sum_pairs_efficient]:
    test.expect(func(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
    test.expect(func(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
    test.expect(func(l3, -7) is None, "No Match: %s should return None for sum = -7" % l3)
    test.expect(func(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
    test.expect(func(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
    test.expect(func(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
    test.expect(func(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
    test.expect(func(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
    test.expect(func(l9, 2) == [1, 1], "Break early if match found for %s -- should return [1, 1] for sum = 2 " % l9)
