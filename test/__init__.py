import typing
from datetime import datetime
from typing import Any


def expect(b: bool, msg: str) -> None:
    if not b:
        raise AssertionError(msg)


def assert_equals(got: Any, want: Any) -> None:
    if got != want:
        raise AssertionError('Got `{}` want `{}`'.format(got, want))


def timed(f: typing.Callable) -> typing.Callable:
    def inner(*args, **kwargs):
        start = datetime.now()
        try:
            return f(*args, **kwargs)
        finally:
            print('Time taken is with args {} and kwargs {} is {}'.format(args, kwargs, datetime.now() - start))
    return inner
