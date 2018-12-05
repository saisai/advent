from common import read_line

raw = bytearray(read_line(), "ascii")


def find_mid(data, swapped):
    i = 0

    while i < len(data) - 1:
        if data[i] == swapped[i + 1]:
            return i

        i += 1


def find_bounds(data, swapped, mid):
    size = 0

    while mid > size and data[mid - size - 1] == swapped[mid + size + 2]:
        size += 1

    return mid - size, mid + size + 2


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


print(len(react(read_line())))
