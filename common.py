import inspect
from pathlib import Path


def _get_input(name):
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / name


def read_line(name="input.txt"):
    with open(_get_input(name)) as f:
        return next(f).strip("\n")


def read_lines(name="input.txt"):
    with open(_get_input(name)) as f:
        return [l for l in (l.strip("\n") for l in f) if l]


def around(x, y):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


def bounds(coords):
    xs = sorted(c[0] for c in coords)
    ys = sorted(c[1] for c in coords)
    return xs[0], ys[0], xs[-1], ys[-1]


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
