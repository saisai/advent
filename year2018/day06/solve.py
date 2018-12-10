from collections import Counter
from collections import deque

from common import around
from common import bounds
from common import manhattan
from common import read_lines


def parse():
    return [(int(x), int(y)) for x, y in (line.split(", ", 1) for line in read_lines())]


def flood(coords):
    grid = {coord: (cid, 0) for cid, coord in enumerate(coords)}
    gl, gt, gr, gb = bounds(coords)

    for cid, coord in enumerate(coords):
        cx, cy = coord
        seen = {coord}
        q = deque(around(cx, cy))

        while q:
            coord = q.popleft()
            x, y = coord

            if coord in seen or not ((gl <= x <= gr) and (gt <= y <= gb)):
                continue

            seen.add(coord)
            dist = manhattan(cx, cy, x, y)
            gcid, gdist = grid.get(coord, (None, None))

            if gcid is None or gdist > dist:
                grid[coord] = (cid, dist)
                q.extend(around(x, y))
            elif gdist == dist:
                grid[coord] = (-1, dist)

    return grid


def largest_area(grid):
    gl, gt, gr, gb = bounds(grid.keys())
    infinite = {
        cid for (x, y), (cid, _) in grid.items() if x in {gl, gr} or y in {gt, gb}
    }
    areas = Counter(cid for cid, _ in grid.values() if cid not in infinite)
    return areas.most_common(1)[0][1]


def manhattan_sum(coords, x, y):
    return sum(manhattan(cx, cy, x, y) for cx, cy in coords)


def intersect(coords, total_dist=10000):
    grid = {}
    q = deque(coords)

    while q:
        coord = q.popleft()
        x, y = coord

        if coord in grid:
            continue

        dist = manhattan_sum(coords, x, y)

        if dist < total_dist:
            grid[coord] = dist
            q.extend(around(x, y))

    return grid


print(largest_area(flood(parse())))
print(len(intersect(parse())))
