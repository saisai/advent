import inspect
from pathlib import Path


def _get_input():
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / "input.txt"


def read_line():
    with open(_get_input()) as f:
        return next(f).strip("\n")


def read_lines():
    with open(_get_input()) as f:
        return [l for l in (l.strip("\n") for l in f) if l]
