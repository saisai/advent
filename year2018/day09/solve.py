from collections import defaultdict
from collections import deque
from itertools import cycle


def play(players, marbles):
    player_gen = cycle(range(1, players + 1))
    marble_gen = iter(range(marbles + 1))
    circle = deque()
    circle.append(next(marble_gen))
    scores = defaultdict(int)

    for player, marble in zip(player_gen, marble_gen):
        if not marble % 23:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return scores


print(max(play(425, 70848).values()))
print(max(play(425, 7084800).values()))
