import re


def part1():
    tree_lines = []
    with open("./day3.input") as file_input:
        for line in file_input.readlines():
            tree_lines.append(line.strip())

    total_collisions = 0
    n = len(tree_lines)
    x, y = (0, 0)
    dx, dy = (3, 1)
    while y < n:
        x %= len(tree_lines[0])
        if tree_lines[y][x] == "#":
            total_collisions += 1
        x += dx
        y += dy
    print(total_collisions)


def part2():
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
