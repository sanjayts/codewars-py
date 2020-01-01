# https://www.codewars.com/kata/calculating-with-functions/train/python
import test


# Each number can either be called using an operation like `plus` or without any arguments. For the first case, we need
# a mechanism to carry the state across multiple chained calls which we do here using a lambda -- one level/op at a time
# For the second case, we simply return the literal number.
def _handle(number, arg=None):
    if arg is None:
        return number
    else:
        return arg(number)


def zero(arg=None):
    return _handle(0, arg)


def one(arg=None):
    return _handle(1, arg)


def two(arg=None):
    return _handle(2, arg)


def three(arg=None):
    return _handle(3, arg)


def four(arg=None):
    return _handle(4, arg)


def five(arg=None):
    return _handle(5, arg)


def six(arg=None):
    return _handle(6, arg)


def seven(arg=None):
    return _handle(7, arg)


def eight(arg=None):
    return _handle(8, arg)


def nine(arg=None):
    return _handle(9, arg)


def plus(arg=None):
    return lambda x: x + arg


def minus(arg=None):
    return lambda x: x - arg


def times(arg=None):
    return lambda x: x * arg


def divided_by(arg=None):
    return lambda x: x // arg


test.assert_equals(one(plus(one(plus(one())))), 3)
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
