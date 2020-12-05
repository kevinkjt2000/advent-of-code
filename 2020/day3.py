from functools import reduce
from operator import mul


def product(collection):
    return reduce(mul, collection, 1)


def part1(dx, dy):
    tree_lines = []
    with open("./day3.input") as file_input:
        for line in file_input.readlines():
            tree_lines.append(line.strip())

    total_collisions = 0
    n = len(tree_lines)
    x, y = (0, 0)
    while y < n:
        x %= len(tree_lines[0])
        if tree_lines[y][x] == "#":
            total_collisions += 1
        x += dx
        y += dy
    return total_collisions


def part2():
    return product([
        part1(1, 1),
        part1(3, 1),
        part1(5, 1),
        part1(7, 1),
        part1(1, 2),
    ])


def main():
    print(part2())


if __name__ == "__main__":
    main()
