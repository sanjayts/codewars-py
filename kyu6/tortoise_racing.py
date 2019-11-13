
def race(v1, v2, g):
    if v1 > v2:
        return None

    total_sec = int((g * 60 ** 2) / (v2 - v1))
    hr, rem = divmod(total_sec, 60**2)
    minutes, sec = divmod(rem, 60)
    return [hr, minutes, sec]


print(race(80, 91, 37))
