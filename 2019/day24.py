def biodiversity_rating(layout):
    pow2 = 1
    total = 0
    for line in layout:
        for ch in line:
            if ch == "#":
                total += pow2
            pow2 *= 2
    return total


def compute_next_gen(layout):
    next_layout = []
    for y, line in enumerate(layout):
        next_line = ""
        for x, ch in enumerate(line):
            bug_neighbors = 0
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if y+dy < 0 or len(layout) <= y+dy or x+dx < 0 or len(layout[y]) <= x+dx:
                    continue
                if layout[y+dy][x+dx] == "#":
                    bug_neighbors += 1
            if ch == "#":
                if bug_neighbors == 1:
                    next_line += "#"
                else:
                    next_line += "."
            elif ch == ".":
                if bug_neighbors == 1 or bug_neighbors == 2:
                    next_line += "#"
                else:
                    next_line += "."
        next_layout.append(next_line)
    print("\n".join(next_layout))
    print()

    return next_layout


def part1(layout):
    encountered = set()
    while "".join(layout) not in encountered:
        encountered.add("".join(layout))
        layout = compute_next_gen(layout)
    print(biodiversity_rating(layout))


def main():
    part1(open("day24.input", "r").read().splitlines())
    part1("""....#
#..#.
#..##
..#..
#....""".splitlines())


if __name__ == "__main__":
    main()
