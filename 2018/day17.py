from enum import Enum
from queue import Queue
DEBUG = True


def main():
    real_input = open("day17.input").read().strip().splitlines()
    example = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
    """.strip().splitlines()

    solve_problem(example)
    # solve_problem(real_input)


class GridTile(Enum):
    SAND = "."
    FLOWING = "|"
    WATER = "~"
    CLAY = "#"

    def __repr__(self):
        return self.value


def solve_problem(lines):
    clay_locations = find_clay_locations(lines)
    max_x, max_y, min_x = min_max_clay_adjustment(clay_locations)
    water_grid = create_water_grid_with_clay_placements(max_x, max_y, clay_locations)

    print_grid(water_grid)

    while pump_water(min_x, water_grid, max_x, max_y):
        print_grid(water_grid)
        print_num_water_tiles(water_grid)
        import pdb; pdb.set_trace()  # XXX BREAKPOINT

    print_grid(water_grid)
    print_num_water_tiles(water_grid)

def pump_water(min_x, water_grid, max_x, max_y):
    x, y = (500 + 1 - min_x, 0)

    q = Queue()
    q.put((x, y))
    while not q.empty():
        x, y = q.get()
        if x < 0 or max_x + 1 < x or y < 0 or max_y < y:
            continue
        if water_grid[y][x] == GridTile.FLOWING:
            q.put((x, y + 1))
            continue
        elif water_grid[y][x] == GridTile.SAND:
            water_grid[y][x] = GridTile.FLOWING
            return True

        if water_grid[y][x] in [GridTile.CLAY, GridTile.WATER]:
            if water_grid[y - 1][x] == GridTile.FLOWING:
                blocked_left = True
                blx = x
                while True:
                    left = GridTile.SAND
                    if 0 < blx:
                        left = water_grid[y - 1][blx - 1]
                    if left == GridTile.SAND:
                        blocked_left = False
                        break
                    if left in [GridTile.WATER, GridTile.CLAY]:
                        break
                    blx -= 1

                blocked_right = True
                brx = x
                while True:
                    right = GridTile.SAND
                    if brx < max_x + 1:
                        right = water_grid[y - 1][brx + 1]
                    if right == GridTile.SAND:
                        blocked_right = False
                        break
                    if right in [GridTile.WATER, GridTile.CLAY]:
                        break
                    brx += 1

                if blocked_left and blocked_right:
                    water_grid[y - 1][x] = GridTile.WATER
                    return True
                q.put((x - 1, y - 1))
                q.put((x + 1, y - 1))
    return False

def print_num_water_tiles(water_grid):
    num_water_tiles = 0
    for y in range(1, len(water_grid)):
        for tile in water_grid[y]:
            if tile in [GridTile.WATER, GridTile.FLOWING]:
                num_water_tiles += 1
    print(num_water_tiles)

def create_water_grid_with_clay_placements(max_x, max_y, clay_locations):
    water_grid = [[GridTile.SAND for x in range(max_x + 2)] for y in range(max_y + 1)]
    for loc in clay_locations:
        for x in loc[0]:
            for y in loc[1]:
                water_grid[y + 1][x + 1] = GridTile.CLAY
    return water_grid

def min_max_clay_adjustment(clay_locations):
    min_x = min([coord[0].start for coord in clay_locations])
    min_y = min([coord[1].start for coord in clay_locations])

    for i, loc in enumerate(clay_locations):
        clay_locations[i] = (
            range(loc[0].start - min_x, loc[0].stop - min_x),
            range(loc[1].start - min_y, loc[1].stop - min_y),
        )

    max_x = max([coord[0].stop for coord in clay_locations])
    max_y = max([coord[1].stop for coord in clay_locations])
    return max_x, max_y, min_x


def print_grid(water_grid):
    if not DEBUG:
        return
    for row in water_grid:
        print("".join([repr(x) for x in row]))
    print("")


def find_clay_locations(lines):
    clay_locations = []
    for line in lines:
        left, right = line.split(", ")
        if "x" in left:
            _, x = left.split("=")
            _, y = right.split("=")
            x = range(int(x), int(x) + 1)
            y = range(*[int(num) for num in y.split("..")])
            y = range(y.start, y.stop + 1)
        else:
            _, y = left.split("=")
            _, x = right.split("=")
            x = range(*[int(num) for num in x.split("..")])
            x = range(x.start, x.stop + 1)
            y = range(int(y), int(y) + 1)
        clay_locations.append((x, y))
    return clay_locations


if __name__ == "__main__":
    main()
