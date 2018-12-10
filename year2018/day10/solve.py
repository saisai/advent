import re

import attr

from common import bounds
from common import read_lines


@attr.s(auto_attribs=True, frozen=True)
class Point:
    x: int
    y: int
    dx: int
    dy: int

    @property
    def coord(self):
        return self.x, self.y

    def step(self):
        return type(self)(self.x + self.dx, self.y + self.dy, self.dx, self.dy)


def parse(lines):
    return [
        Point(*values)
        for values in ((int(x) for x in re.findall(r"-?\d+", line)) for line in lines)
    ]


def step(points):
    return [point.step() for point in points]


def score_area(points):
    left, top, right, bottom = bounds(tuple(point.coord for point in points))
    return abs(right - left) * abs(bottom - top)


def find_message(points):
    best_score = 2 ** 64
    best_points = None
    seconds = 0

    for i in range(100_000):
        score = score_area(points)

        if score < best_score:
            best_score = score
            best_points = points
            seconds = i
        elif score >= best_score:
            break

        points = step(points)

    return seconds, best_points


def draw_message(seconds, points):
    coords = {point.coord for point in points}
    left, top, right, bottom = bounds(coords)
    lines = []

    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            lines.append("X" if (x, y) in coords else ".")

        lines.append("\n")

    print("".join(lines))
    print(f"{seconds} seconds")


draw_message(*find_message(parse(read_lines())))
