from collections import Counter
from collections import deque

from common import read_lines


def parse():
    return [(int(x), int(y)) for x, y in (line.split(", ", 1) for line in read_lines())]


def bounds(coords):
    xs = sorted(c[0] for c in coords)
    ys = sorted(c[1] for c in coords)
    return xs[0], ys[0], xs[-1], ys[-1]


def around(x, y):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


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
            dist = abs(cx - x) + abs(cy - y)
            gcid, gdist = grid.get(coord, (None, None))

            if gcid is None or gdist > dist:
                grid[coord] = (cid, dist)
                q.extend(around(x, y))
            elif gdist == dist:
                grid[coord] = (-1, dist)

    return grid


def draw(grid):
    gl, gt, gr, gb = bounds(grid.keys())

    for y in range(gt, gb + 1):
        for x in range(gl, gr + 1):
            cid, dist = grid[x, y]
            print(f"{' ' if dist else '*'}{cid:02} ", end="")

        print()


def largest_area(grid):
    gl, gt, gr, gb = bounds(grid.keys())
    infinite = {
        cid for (x, y), (cid, _) in grid.items() if x in {gl, gr} or y in {gt, gb}
    }
    areas = Counter(cid for cid, _ in grid.values() if cid not in infinite)
    return areas.most_common(1)[0]


filled = flood(parse())
print(largest_area(filled))
