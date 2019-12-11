from intcode import run_program


def solve(data):
    y, x = 0, 0
    dy, dx = 1, 0
    panels = {(0, 0): 1}
    def camera_input():
        while True:
            yield panels.get((y, x), 0)
    outputs = run_program(map(int, data.split(",")), camera_input)
    while True:
        try:
            color_to_paint = next(outputs)
            direction_change = next(outputs)
            panels[(y, x)] = color_to_paint
            if direction_change == 0:
                if dy == 1 and dx == 0:
                    dy, dx = 0, -1
                elif dy == 0 and dx == -1:
                    dy, dx = -1, 0
                elif dy == -1 and dx == 0:
                    dy, dx = 0, 1
                else:
                    dy, dx = 1, 0
            else:
                if dy == 1 and dx == 0:
                    dy, dx = 0, 1
                elif dy == 0 and dx == -1:
                    dy, dx = 1, 0
                elif dy == -1 and dx == 0:
                    dy, dx = 0, -1
                else:
                    dy, dx = -1, 0
            y += dy
            x += dx
        except StopIteration:
            break
    print(len(panels))
    white_pixels = [(y, x) for (y, x) in panels if panels[(y, x)] == 1]
    for y, x in white_pixels:
        print(y, x)


def main():
    solve(open("day11.input").read())


if __name__ == "__main__":
    main()
