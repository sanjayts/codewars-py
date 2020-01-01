# https://www.codewars.com/kata/strip-comments/train/python

import test
import re
from typing import List


def solution(s: str, markers: List[str]) -> str:
    parts = s.split('\n')
    new_parts = []
    for p in parts:
        # The below filtering is to ensure that we correctly handle cases wherein two separators occur back to back.
        # E.g. "abc!# " should strip both ! and #. Simply doing min or max will yield incorrect results unless we filter
        # out non-matches denoted by -1
        indices = [p.find(sep) for sep in markers if p.find(sep) > -1]
        if indices:
            idx = min(indices)
            new_parts.append(p[:idx].strip())
        else:
            new_parts.append(p)
    return '\n'.join(new_parts)


# Regex based easy solution
def solution_regex(s: str, markers: List[str]) -> str:
    pattern = r'''
    \ *?    # 0 or more space before the marker, the \ is to ensure we escape # and space( )
    \{}     # the marker char
    .*      # any trailing spaces after the marker
    $       # match end of newline (not line since we use the re.M flag
    '''
    for m in markers:
        s = re.sub(pattern.format(m), '', s, flags=re.M | re.VERBOSE)
    return s


test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas!#", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

test.assert_equals(solution_regex("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution_regex("apples, pears # and bananas\ngrapes\nbananas!#", ["#", "!"]), "apples, pears\ngrapes\nbananas")
test.assert_equals(solution_regex("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")