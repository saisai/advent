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


print(sum_metadata(build(read_line())))
