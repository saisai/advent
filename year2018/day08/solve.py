from itertools import count
from itertools import repeat

from common import read_line


def build(line):
    reader = (int(x) for x in line.split())
    nid_gen = count()
    nodes = {}
    ops = [(next(nid_gen), "node")]

    while ops:
        nid, op = ops.pop()

        if op == "node":
            nodes[nid] = {"children": [], "metadata": []}
            child_count = next(reader)
            meta_count = next(reader)
            ops.extend(repeat((nid, "meta"), meta_count))
            child_nids = [next(nid_gen) for _ in range(child_count)]

            for child_nid in reversed(child_nids):
                nodes[nid]["children"].insert(0, child_nid)
                ops.append((child_nid, "node"))

        elif op == "meta":
            nodes[nid]["metadata"].append(next(reader))

    return nodes


def sum_metadata(nodes):
    return sum(x for node in nodes.values() for x in node["metadata"])


def node_values(nodes):
    values = {
        nid: sum(node["metadata"])
        for nid, node in nodes.items()
        if not node["children"]
    }
    todo = [0]

    while todo:
        nid = todo.pop()

        if nid in values:
            continue

        node = nodes[nid]
        need = [cid for cid in node["children"] if cid not in values]

        if need:
            todo.append(nid)
            todo.extend(need)
        else:
            child_count = len(node["children"])
            values[nid] = sum(
                values[node["children"][i - 1]]
                for i in node["metadata"]
                if 0 < i <= child_count
            )

    return values


nodes = build(read_line())
print(sum_metadata(nodes))
print(node_values(nodes)[0])
