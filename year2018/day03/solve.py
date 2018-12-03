import re
from collections import Counter

import attr

from common import read_lines


@attr.s(auto_attribs=True)
class Claim:
    id: int
    left: int
    top: int
    width: int
    height: int

    _line_re = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")

    @classmethod
    def from_line(cls, line):
        m = cls._line_re.match(line)
        return cls(*[int(g) for g in m.groups()])

    @property
    def x_range(self):
        return range(self.left, self.left + self.width)

    @property
    def y_range(self):
        return range(self.top, self.top + self.height)

    def __iter__(self):
        for x in self.x_range:
            for y in self.y_range:
                yield x, y

    def intact(self, point_counts):
        return all(point_counts[point] == 1 for point in self)


data = [Claim.from_line(line) for line in read_lines()]
point_counts = Counter([point for claim in data for point in claim])
print(sum(count > 1 for count in point_counts.values()))

for claim in data:
    if claim.intact(point_counts):
        print(claim)
        break
