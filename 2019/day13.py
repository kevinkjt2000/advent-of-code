import sys
from intcode import run_program


def solve(data):
    tiles = {}
    def joystick():
        while True:
            print_tiles(tiles)
            paddle = [p for p in tiles if tiles[p] == 3][0]
            ball = [p for p in tiles if tiles[p] == 4][0]
            dist = abs(paddle[1] - ball[1])
            if dist == 0:
                yield 0
            elif ball[1] < paddle[1]:
                yield -1
            else:
                yield 1
    program = list(map(int, data.split(",")))
    program[0] = 2
    outputs = run_program(program, joystick)
    score = 0
    while True:
        try:
            x = next(outputs)
            y = next(outputs)
            tile = next(outputs)
            if (y, x) == (0, -1):
                score = tile
                print("Score:", score)
                print_tiles(tiles)
            else:
                tiles[(y, x)] = tile
        except StopIteration:
            break
    print(len(tiles))
    block_tiles = [(y, x) for (y, x) in tiles if tiles[(y, x)] == 2]
    print(len(block_tiles))


def print_tiles(tiles):
    min_x = min(x for _y, x in tiles)
    prev_y = None
    prev_x = None
    for y, x in sorted(tiles, key=lambda p: (-p[0], p[1])):
        if y != prev_y:
            print()
            sys.stdout.write(" " * abs(min_x - x))
            prev_y = y
            prev_x = x
        if x != prev_x + 1:
            sys.stdout.write(" " * (abs(prev_x - x) - 1))
        sys.stdout.write(str(tiles[(y, x)]))
        prev_x = x
    print()


def main():
    solve(open("day13.input").read())


if __name__ == "__main__":
    main()
