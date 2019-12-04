def solve(wires, first_steps):
    left, right = wires
    left_fs, right_fs = first_steps
    collisions = left.intersection(right)
    print(sorted(collisions, key=lambda p: abs(p[0]) + abs(p[1]))[1])
    lowest_steps = sorted(collisions, key=lambda p: left_fs[p] + right_fs[p])[1]
    print(left_fs[lowest_steps] + right_fs[lowest_steps])


def parse_input(text):
    lines = text.strip().splitlines()
    wires = []
    first_steps = []
    for turns in lines:
        x, y = 0, 0
        steps = 0
        first_step = {}
        wire = set()
        for turn in turns.split(","):
            direction, amount = turn[0], int(turn[1:])
            dx = 0
            dy = 0
            if direction == "R":
                dx = 1
            elif direction == "L":
                dx = -1
            elif direction == "U":
                dy = 1
            elif direction == "D":
                dy = -1
            for i in range(amount):
                wire.add((x, y))
                if (x, y) not in first_step:
                    first_step[(x, y)] = steps
                x += dx
                y += dy
                steps += 1
        wires.append(wire)
        first_steps.append(first_step)

    return wires, first_steps


def main():
    example = parse_input("""R8,U5,L5,D3
U7,R6,D4,L4""")
    solve(*example)

    real_input = parse_input(open("day3.input").read())
    result = solve(*real_input)


main()
