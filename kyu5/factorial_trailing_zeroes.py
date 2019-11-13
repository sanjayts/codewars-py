# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python

from math import floor, log


# Looking at existing solutions, I realized that the simplest way to find the trailing zero count is to
# recursive divide the number by 5 and add them up!
# https://www.purplemath.com/modules/factzero.htm
def zeros(n: int) -> int:
    kmax = floor(log(n, 5))
    num = sum(floor(n / 5 ** k) for k in range(1, kmax + 1))
    return num


assert zeros(30) == 7
