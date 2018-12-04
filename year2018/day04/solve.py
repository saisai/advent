from collections import Counter
from collections import defaultdict
from datetime import datetime

from common import read_lines


def get_minutes(data):
    index = defaultdict(Counter)
    guard_id = None
    asleep = None

    for line in data:
        date_str, note = line[1:].split("] ")
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        first, *rest = note.split()

        if first == "Guard":
            assert asleep is None
            guard_id = int(rest[0][1:])
        elif first == "falls":
            assert asleep is None
            asleep = date
        elif first == "wakes":
            index[guard_id].update(range(asleep.minute, date.minute))
            asleep = None

    return index


def strat_one(minutes):
    id, counts = max(minutes.items(), key=lambda x: sum(x[1].values()))
    minute = counts.most_common(1)[0][0]
    print(id, minute, id * minute)


def strat_two(minutes):
    def extract():
        for id, counts in minutes.items():
            yield id, counts.most_common(1)[0]

    id, (minute, count) = max(extract(), key=lambda x: x[1][1])
    print(id, minute, count, id * minute)


data = get_minutes(sorted(read_lines()))
strat_one(data)
strat_two(data)
