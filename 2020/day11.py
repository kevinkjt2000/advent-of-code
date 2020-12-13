from copy import deepcopy

EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"


def read_input():
    with open("./day11.input") as file_input:
        return [[c for c in line.strip()] for line in file_input.readlines()]


def part1():
    layout = read_input()
    next_layout = None
    while layout != next_layout:
        next_layout = deepcopy(layout)
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == FLOOR:
                    continue
                neighbor_count = 0
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if i + di in range(len(layout)) and j + dj in range(len(layout[0])):
                        if layout[i+di][j+dj] == OCCUPIED:
                            neighbor_count += 1
                if layout[i][j] == EMPTY and neighbor_count == 0:
                    next_layout[i][j] = OCCUPIED
                elif layout[i][j] == OCCUPIED and neighbor_count >= 4:
                    next_layout[i][j] = EMPTY
        layout, next_layout = next_layout, layout
    print(sum(row.count(OCCUPIED) for row in layout))


def part2():
    layout = read_input()
    next_layout = None
    while layout != next_layout:
        next_layout = deepcopy(layout)
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if layout[i][j] == FLOOR:
                    continue
                neighbor_count = 0
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    i_, j_ = i, j
                    while i_ + di in range(len(layout)) and j_ + dj in range(len(layout[0])):
                        if layout[i_+di][j_+dj] == OCCUPIED:
                            neighbor_count += 1
                            break
                        if layout[i_+di][j_+dj] == EMPTY:
                            break
                        i_ += di
                        j_ += dj
                if layout[i][j] == EMPTY and neighbor_count == 0:
                    next_layout[i][j] = OCCUPIED
                elif layout[i][j] == OCCUPIED and neighbor_count >= 5:
                    next_layout[i][j] = EMPTY
        layout, next_layout = next_layout, layout
    print(sum(row.count(OCCUPIED) for row in layout))


part2()
