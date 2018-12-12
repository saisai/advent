from itertools import chain

from more_itertools import windowed

from common import read_lines


def parse(lines):
    pots = tuple(c == "#" for c in lines[0].split(": ")[1])
    notes = {
        tuple(c == "#" for c in key): value == "#"
        for key, value in (note.split(" => ") for note in lines[1:])
    }
    return pots, notes


_extra = (False,) * 5


def run(lines, steps=20):
    pots, notes = parse(lines)

    for _ in range(1, steps + 1):
        pots = tuple(
            notes.get(items, False)
            for items in windowed(chain(_extra, pots, _extra), 5)
        )

    offset = 3 * steps
    return sum(c * (i - offset) for i, c in enumerate(pots))


print(run(read_lines("input.txt")))
