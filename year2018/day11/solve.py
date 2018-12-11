from itertools import product


def digit(value, place):
    return value // place % 10


def make_grid(sn):
    grid = {}

    for x, y in product(range(300), repeat=2):
        grid[x, y] = digit(((x + 11) * (y + 1) + sn) * (x + 11), 100) - 5

    return grid


def find_square(grid):
    best_coord = None
    best_power = 0

    for left, top in product(range(1, 298), repeat=2):
        power = sum(grid[left + dx, top + dy] for dx, dy in product(range(3), repeat=2))

        if power > best_power:
            best_coord = left, top
            best_power = power

    left, top = best_coord
    return left + 1, top + 1


grid = make_grid(4172)
print(find_square(grid))
