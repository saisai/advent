from collections import Counter
from functools import lru_cache
from itertools import combinations

from common import read_lines

data = read_lines()

twos = 0
threes = 0

for item in data:
    counts = Counter(item).values()

    if 2 in counts:
        twos += 1

    if 3 in counts:
        threes += 1

print(twos, threes, twos * threes)


@lru_cache(len(data))
def positions(item):
    return set(enumerate(item))


for a, b in combinations(data, 2):
    diff = positions(a) ^ positions(b)

    if len(diff) == 2:
        i = next(iter(diff))[0]
        print(a, b, i, a[:i] + a[i + 1 :])
        break
