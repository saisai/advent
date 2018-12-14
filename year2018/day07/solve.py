from bisect import insort_left
from collections import defaultdict

from networkx import DiGraph
from networkx import lexicographical_topological_sort

from common import read_lines


def parse(lines):
    return DiGraph(
        sorted((parts[1], parts[7]) for parts in (line.split() for line in lines))
    )


graph = parse(read_lines())
print("".join(lexicographical_topological_sort(graph)))


def build(graph, workers=5, base_cost=60):
    base_cost -= ord("A") - 1
    incomplete = set(graph.nodes)
    available = sorted(n for n, d in graph.in_degree if d == 0)
    schedule = defaultdict(list)
    time = 0

    while incomplete:
        done = schedule.pop(time, ())
        incomplete.difference_update(done)
        workers += len(done)

        for done_node in done:
            for next_node in graph.successors(done_node):
                if not set(graph.predecessors(next_node)).intersection(incomplete):
                    insort_left(available, next_node)

        while workers and available:
            node = available.pop(0)
            workers -= 1
            schedule[time + base_cost + ord(node)].append(node)

        time = min(schedule.keys(), default=time)

    return time


print(build(graph))
