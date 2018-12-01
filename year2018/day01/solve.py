from itertools import cycle

from common import read_lines

data = [int(x) for x in read_lines()]
print(sum(x for x in data))

seen = set()
current = 0

for item in cycle(data):
    current += item

    if current in seen:
        print(current)
        break

    seen.add(current)
