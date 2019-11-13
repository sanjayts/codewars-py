
def rgb(r, g, b):
    normalized = (min(x, 255) if x > 0 else 0 for x in [r, g, b])
    g = (hex(c).replace('0x', '') for c in normalized)
    return ''.join(c if len(c) == 2 else '0'+c for c in g).upper()


def rgb_format(r, g, b):
    normalized = (min(x, 255) if x > 0 else 0 for x in [r, g, b])
    return ''.join('{:02X}'.format(c) for c in normalized)

print(rgb(0,0,0))

print(rgb_format(9, 260, 30))