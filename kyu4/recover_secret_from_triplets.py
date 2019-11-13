# https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets/train/python
from typing import List, Dict, NamedTuple


class CharNode(object):

    def __init__(self, ch: str):
        self.ch = ch
        self.children = set()
        self.parents = set()

    def add_child(self, child: 'CharNode'):
        self.children.add(child)
        child.parents.add(self)


def _get_node(ch: str, cache: Dict[str, CharNode]) -> CharNode:
    if ch in cache:
        return cache[ch]
    else:
        n = CharNode(ch)
        cache[ch] = n
        return n


def recur(start: CharNode) -> str:
    buf = []
    visited = set()
    nodes = [start]
    while len(nodes) > 0:
        cur = nodes.pop()
        buf.append(cur.ch)
        visited.add(cur)
        for c in cur.children:
            all_visited = all((p in visited) for p in c.parents)
            if len(c.parents) == 1 or all_visited:
                nodes.append(c)
    return ''.join(buf)


def recoverSecret(triplets: List[List[str]]) -> str:
    cache = {}
    for row in triplets:
        n1, n2, n3 = [_get_node(ch, cache) for ch in row]
        n1.add_child(n2)
        n2.add_child(n3)

    root = next(n for n in cache.values() if len(n.parents) == 0)
    secret = recur(root)
    return secret


arr = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]
print(recoverSecret(arr))
