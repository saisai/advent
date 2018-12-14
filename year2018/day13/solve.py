from __future__ import annotations

from itertools import cycle
from typing import Generator

import attr

from common import read_lines

turn_order = ("l", "s", "r")
turns = {
    "l": {"^": ("-", "<"), ">": ("|", "^"), "v": ("-", ">"), "<": ("|", "v")},
    "r": {"^": ("-", ">"), ">": ("|", "v"), "v": ("-", "<"), "<": ("|", "^")},
    "s": {"^": ("|", "^"), ">": ("-", ">"), "v": ("|", "v"), "<": ("-", "<")},
}


@attr.s(auto_attribs=True, cmp=False)
class Cart:
    x: int
    y: int
    dir: str
    crash: bool = False
    turn: Generator[str] = attr.Factory(lambda: cycle(turn_order))

    def move(self, track, carts):
        if self.crash:
            return

        coord = self.x, self.y
        carts.pop(coord)
        c = track[coord]

        name, delta, next_dir = steps[c, self.dir]

        if name is None:
            c, self.dir = turns[next(self.turn)][self.dir]
            name, delta, next_dir = steps[c, self.dir]

        setattr(self, name, getattr(self, name) + delta)
        self.dir = next_dir
        coord = self.x, self.y

        if coord in carts:
            self.crash = True
            carts.pop(coord).crash = True
        else:
            carts[coord] = self


steps = {
    ("|", "^"): ("y", -1, "^"),
    ("|", "v"): ("y", 1, "v"),
    ("-", ">"): ("x", 1, ">"),
    ("-", "<"): ("x", -1, "<"),
    ("/", "^"): ("x", 1, ">"),
    ("/", ">"): ("y", -1, "^"),
    ("/", "v"): ("x", -1, "<"),
    ("/", "<"): ("y", 1, "v"),
    ("\\", "^"): ("x", -1, "<"),
    ("\\", ">"): ("y", 1, "v"),
    ("\\", "v"): ("x", 1, ">"),
    ("\\", "<"): ("y", -1, "^"),
    ("+", "^"): (None, None, None),
    ("+", ">"): (None, None, None),
    ("+", "v"): (None, None, None),
    ("+", "<"): (None, None, None),
}


def parse(lines):
    track = {}
    carts = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in "^>v<":
                carts[x, y] = Cart(x, y, c)
                c = "-" if c in "><" else "|"
            track[x, y] = c

    return track, carts


def run(lines):
    track, carts = parse(lines)
    first_crash = False

    while len(carts) > 1:
        order = sorted(carts.values(), key=lambda c: (c.y, c.x))

        for cart in order:
            cart.move(track, carts)

            if cart.crash:
                if not first_crash:
                    first_crash = True
                    print(cart)

    print(next(iter(carts.values())))


run(read_lines("input.txt"))
