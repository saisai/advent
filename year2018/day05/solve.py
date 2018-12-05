from common import read_line


def react(line):
    out = []

    for c in line:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)

    return out


def remove_react(line):
    sizes = {}

    for c in set(line.lower()):
        removed = line.replace(c, "").replace(c.upper(), "")
        sizes[c] = len(react(removed))

    return min(sizes.items(), key=lambda x: x[1])


data = read_line()
print(len(react(data)))
print(remove_react(data))
