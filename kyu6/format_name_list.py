from typing import List, Dict


def namelist(seq_of_dct: List[Dict[str, str]]) -> str:
    names = [d['name'] for d in seq_of_dct]
    buf, sz = [], len(names)
    for i, name in enumerate(names):
        if i == sz - 1:
            buf.append(name)
        elif i == sz - 2:
            buf.append('%s & ' % name)
        else:
            buf.append('%s, ' % name)
    return ''.join(buf)


out = namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
print(out)
