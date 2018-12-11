from functools import partial
from itertools import product
from multiprocessing.pool import Pool
from operator import itemgetter


def digit(value, place):
    return value // place % 10


def make_grid(sn):
    grid = {}

    for x, y in product(range(300), repeat=2):
        grid[x, y] = digit(((x + 11) * (y + 1) + sn) * (x + 11), 100) - 5

    return grid


def find_square(grid):
    powers = {}

    for left, top in product(range(298), repeat=2):
        powers[left, top] = sum(
            grid[left + dx, top + dy] for dx, dy in product(range(3), repeat=2)
        )

    left, top = max(powers, key=lambda key: powers[key])
    return left + 1, top + 1


def find_square_size_single(grid, left, top):
    power = grid[left, top]
    powers = {0: power}

    for size in range(1, 300):
        if left + size >= 300 or top + size >= 300:
            break

        power += sum(grid[left + size, top + dy] for dy in range(size))
        power += sum(grid[left + dx, top + size] for dx in range(size))
        power += grid[left + size, top + size]
        powers[size] = power

    size, power = max(powers.items(), key=itemgetter(1))
    return left, top, size, power


def find_square_size(grid):
    with Pool() as p:
        results = p.starmap(
            partial(find_square_size_single, grid), product(range(300), repeat=2)
        )

    left, top, size, power = max(results, key=itemgetter(3))
    return left + 1, top + 1, size + 1


grid = make_grid(4172)
print(find_square(grid))
print(find_square_size(grid))
