# https://www.codewars.com/kata/parseint-reloaded/train/python
# INCOMPLETE
import test

_MAPPING = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand',
    1000000: 'million'
}

_NAME_TO_NUMBER = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                   'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                   'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
                   'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
                   'thousand': 1000, 'million': 1000000}


def parse_int(s: str) -> int:
    s = s.replace('and', '')  # strip out all optional ands
    parts = s.split()
    acc, multiplier = 0, 1
    for part in parts:
        if '-' in part:
            p1, p2 = part.split('-')
            acc += (_NAME_TO_NUMBER[p1] * 10 + _NAME_TO_NUMBER[p2])
        else:
            v = _NAME_TO_NUMBER[part]
    return acc


print({v: k for (k, v) in _MAPPING.items()})

test.assert_equals(parse_int('one'), 1)
test.assert_equals(parse_int('twenty'), 20)
test.assert_equals(parse_int('two hundred forty-six'), 246)
test.assert_equals(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"), 783919)
