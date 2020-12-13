def read_input():
    with open("./day12.input") as file_input:
        for line in file_input.readlines():
            line = line.strip()
            yield line[0], int(line[1:])


def part1():
    instructions = list(read_input())
    theta = 0  # facing east
    dx, dy = 0, 0
    for letter, number in instructions:
        if letter == "F":
            letter = {0: "E", 90: "N", 180: "W", 270: "S"}[theta]
        if letter == "N":
            dy += number
        elif letter == "S":
            dy -= number
        elif letter == "E":
            dx += number
        elif letter == "W":
            dx -= number
        elif letter == "L":
            theta = (theta + number) % 360
        elif letter == "R":
            theta = (theta - number) % 360
    return abs(dx) + abs(dy)


def part2():
    instructions = list(read_input())
    dx, dy = 0, 0
    wx, wy = 10, 1
    for letter, number in instructions:
        if letter == "F":
            dx += wx * number
            dy += wy * number
        elif letter == "N":
            wy += number
        elif letter == "S":
            wy -= number
        elif letter == "E":
            wx += number
        elif letter == "W":
            wx -= number
        elif (letter, number) in [("L", 90), ("R", 270)]:
            wx, wy = -wy, wx
        elif (letter, number) in [("L", 180), ("R", 180)]:
            wx, wy = -wx, -wy
        elif (letter, number) in [("L", 270), ("R", 90)]:
            wx, wy = wy, -wx
    return abs(dx) + abs(dy)


# 2458 too low


print(part2())
