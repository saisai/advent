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
    score = 0
    delta = 0

    for i in range(1, steps + 1):
        pots = tuple(
            notes.get(items, False)
            for items in windowed(chain(_extra, pots, _extra), 5)
        )

        offset = 3 * i
        new_score = sum(c * (i - offset) for i, c in enumerate(pots))
        new_delta = new_score - score
        score = new_score

        if new_delta == delta:
            score += (steps - i) * new_delta
            break

        delta = new_delta

    return score


print(run(read_lines("input.txt")))
print(run(read_lines("input.txt"), 50_000_000_000))
