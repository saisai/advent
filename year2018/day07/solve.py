from networkx import DiGraph
from networkx import lexicographical_topological_sort

from common import read_lines


def parse(lines):
    return DiGraph(
        sorted((parts[1], parts[7]) for parts in (line.split() for line in lines))
    )


print("".join(lexicographical_topological_sort(parse(read_lines()))))
