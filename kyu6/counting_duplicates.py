from collections import defaultdict


# A simple direct approach -- not the most efficient but is readable!
def duplicate_count(text: str) -> int:
    dct = defaultdict(int)
    for c in text:
        dct[c.lower()] += 1
    return sum(1 for v in dct.values() if v > 1)


out = duplicate_count("indivisibilityD")
print(out)
