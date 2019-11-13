class Node(object):
    pass


def loop_size(root_node) -> int:
    """
    Iterate over the loop twice -- once when populating the `seen` set and the next time to actually count the elements
    in the loop.
    """
    seen = set()
    cur = root_node
    while cur not in seen:
        seen.add(cur)
        cur = cur.next

    sz = 1
    node = cur.next
    while node != cur:
        sz += 1
        node = node.next
    return sz


nodes = [Node() for _ in range(50)]
for n, next_node in zip(nodes, nodes[1:]):
    n.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]))  # 29
