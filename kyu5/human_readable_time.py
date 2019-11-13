def make_readable(seconds: int) -> str:
    hr, rem = divmod(seconds, 60 ** 2)
    mins, secs = divmod(rem, 60)
    return '{:02}:{:02}:{:02}'.format(hr, mins, secs)


print(make_readable(60))
