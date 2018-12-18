data = open("day17.input").read().strip()
data = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
""".strip()

lines = data.split("\n")

clay_locations = []
for line in lines:
    left, right = line.split(", ")
    if left[0] == "x":
        _, x = left.split("=")
        _, y = right.split("=")
        x = range(int(x), int(x)+1)
        y = range(*[int(num) for num in y.split("..")])
        y = range(y.start, y.stop+1)
    else:
        _, y = left.split("=")
        _, x = right.split("=")
        x = range(*[int(num) for num in x.split("..")])
        x = range(x.start, x.stop+1)
        y = range(int(y), int(y)+1)
    clay_locations.append((x, y))

min_x = min([coord[0].start for coord in clay_locations])
min_y = min([coord[1].start for coord in clay_locations])

for i, loc in enumerate(clay_locations):
    clay_locations[i] = (
        range(loc[0].start - min_x, loc[0].stop - min_x),
        range(loc[1].start - min_y, loc[1].stop - min_y),
    )

max_x = max([coord[0].stop for coord in clay_locations])
max_y = max([coord[1].stop for coord in clay_locations])

from enum import Enum
class GridTile(Enum):
    SAND = "."
    FLOWING = "|"
    WATER = "~"
    CLAY = "#"

    def __repr__(self):
        return self.value

water_grid = [[GridTile.SAND for x in range(max_x + 2)]
              for y in range(max_y + 1)]
for loc in clay_locations:
    for x in loc[0]:
        for y in loc[1]:
            water_grid[y+1][x+1] = GridTile.CLAY

for row in water_grid:
    print("".join([repr(x) for x in row]))
print("")

num_water_tiles = 0
from queue import Queue
while True:  # while the water has not changed
    x, y = (500+1-min_x, 0)

    if 0 < x:
        left = water_grid[y][x-1]
    else:
        left = GridTile.SAND
    if x < max_x +1:
        right = water_grid[y][x+1]
    else:
        right = GridTile.SAND
    if y < max_y:
        down = water_grid[y+1][x]
    else:
        down = GridTile.SAND

    q = Queue()
    qx, qy = x, y
    q.put((x, y))
    modified = False
    iter = 100000
    while not q.empty() and not modified and iter > 0:
        iter -= 1
        qx, qy = q.get()
        if qx < 0 or max_x + 1 < qx or qy < 0 or max_y < qy:
            continue
        if water_grid[qy][qx] == GridTile.FLOWING:
            q.put((qx, qy+1))
        elif water_grid[qy][qx] == GridTile.SAND:
            water_grid[qy][qx] = GridTile.FLOWING
            num_water_tiles += 1
            modified = True
            break

        if water_grid[qy][qx] in [GridTile.CLAY, GridTile.WATER]:
            if water_grid[qy-1][qx] == GridTile.FLOWING:
                blocked_left = True
                blx = qx
                while True:
                    left = GridTile.SAND
                    if 0 < blx:
                        left = water_grid[qy-1][blx-1]
                    if left == GridTile.SAND:
                        blocked_left = False
                        break
                    if left in [GridTile.WATER, GridTile.CLAY]:
                        break
                    blx -= 1

                blocked_right = True
                brx = qx
                while True:
                    right = GridTile.SAND
                    if brx < max_x + 1:
                        right = water_grid[qy-1][brx+1]
                    if right == GridTile.SAND:
                        blocked_right = False
                        break
                    if right in [GridTile.WATER, GridTile.CLAY]:
                        break
                    brx += 1

                if blocked_left and blocked_right:
                    water_grid[qy-1][qx] = GridTile.WATER
                    modified = True
                    break
                q.put((qx-1, qy-1))
                q.put((qx+1, qy-1))


    for row in water_grid:
        print("".join([repr(x) for x in row]))
    print("")

    # water_grid.pop(0)
    # for row in water_grid:
    #     for x in row:
    #         if x in [GridTile.WATER, GridTile.FLOWING]:
    #             num_water_tiles += 1

    if not modified:
        break


for row in water_grid:
    print("".join([repr(x) for x in row]))
print("")
print(num_water_tiles)
