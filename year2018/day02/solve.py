from collections import Counter

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
