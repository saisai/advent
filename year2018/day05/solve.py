from multiprocessing import Pool

from common import read_line


def find_mid(data, swapped):
    i = 0

    while i < len(data) - 1:
        if data[i] == swapped[i + 1]:
            return i

        i += 1


def find_bounds(data, swapped, mid):
    left = mid
    right = mid + 1
    size = len(data)

    while True:
        nl = left - 1
        nr = right + 1

        if nl < 0 or nr == size:
            break

        if data[nl] != swapped[nr]:
            break

        left = nl
        right = nr

    return left, right + 1


def react(data):
    data = bytearray(data, "ascii")
    swapped = data.swapcase()

    while True:
        mid = find_mid(data, swapped)

        if mid is None:
            return data

        left, right = find_bounds(data, swapped, mid)
        del data[left:right]
        del swapped[left:right]


def remove_react_one(data, c):
    removed = data.replace(c, "").replace(c.upper(), "")
    size = len(react(removed))
    return c, size


def remove_react(data):
    with Pool() as p:
        results = p.starmap(remove_react_one, ((data, c) for c in set(data.lower())))

    return min(results, key=lambda x: x[1])


if __name__ == "__main__":
    print(len(react(read_line())))
    print(remove_react(read_line()))
