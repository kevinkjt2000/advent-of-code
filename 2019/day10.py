import itertools
import math
from queue import Queue


example1 = """.#..#
.....
#####
....#
...##"""
expected1 = 8


def count_visible_asteroids(asteroid_map, ay, ax):
    if asteroid_map[ay][ax] == ".":
        return 0
    queue = Queue()
    queue.put((ay-1, ax))
    queue.put((ay+1, ax))
    queue.put((ay, ax-1))
    queue.put((ay, ax+1))
    visited = [[False for col in range(len(asteroid_map[0]))] for row in range(len(asteroid_map))]
    visited[ay][ax] = True
    visible = [[True for col in range(len(asteroid_map[0]))] for row in range(len(asteroid_map))]
    visible[ay][ax] = False
    while not(queue.empty()):
        y, x = queue.get()
        if y < 0 or len(asteroid_map) <= y or x < 0 or len(asteroid_map[0]) <= x:
            continue
        if visited[y][x]:
            continue
        visited[y][x] = True
        queue.put((y-1, x))
        queue.put((y+1, x))
        queue.put((y, x-1))
        queue.put((y, x+1))
        if asteroid_map[y][x] == "#":
            dy, dx = calc_slope(y, x, ay, ax)
            y += dy
            x += dx
            while 0 <= y and y < len(asteroid_map) and 0 <= x and x < len(asteroid_map[0]):
                visible[y][x] = False
                y += dy
                x += dx

    import sys
    num_visible = 0
    for y, row in enumerate(asteroid_map):
        for x, col in enumerate(row):
            if visible[y][x] and asteroid_map[y][x] == "#" and (y != ay or x != ax):
                num_visible += 1
    return num_visible


def calc_slope(y, x, ay, ax):
    dy = y - ay
    dx = x - ax
    gcd = math.gcd(dy, dx)
    if gcd != 0:
        dy //= gcd
        dx //= gcd
    return dy, dx


def calc_distance(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    return math.sqrt((y1 - y2)**2 + (x1 - x2)**2)


def lazer_asteroids(asteroid_map, sy, sx):
    asteroid_locations = []
    print("starting laser")
    for y, row in enumerate(asteroid_map):
        for x, col in enumerate(row):
            if asteroid_map[y][x] == "#" and (y != sy or x != sx):
                asteroid_locations.append((y, x))
    slope_groups = {}
    for y, x in asteroid_locations:
        dy, dx = calc_slope(y, x, sy, sx)
        if (dy, dx) not in slope_groups:
            slope_groups[(dy, dx)] = []
        slope_groups[(dy, dx)].append((y, x))

    # sort slope groups by distance from stationed lazer base
    for sg in slope_groups:
        slope_groups[sg].sort(key=lambda p: calc_distance((sy, sx), p), reverse=True)

    # iterate through slope_groups clockwise
    def slope_sorter(slope):
        dy, dx = slope
        angle = math.atan2(-dy, dx)
        angle = math.pi/2 - angle
        if angle < 0:
            angle = math.pi*2 + angle
        return angle

    clock_order = sorted(slope_groups.keys(), key=slope_sorter)
    lazered_so_far = 0
    for slope in itertools.cycle(clock_order):
        if len(slope_groups[slope]) > 0:
            y, x = slope_groups[slope].pop()
            print(f"shooting {y}, {x}: {slope} {slope_sorter(slope)}")
            lazered_so_far += 1
        if lazered_so_far == 200:
            return (y, x)


def solve(asteroid_map):
    asteroid_map = asteroid_map.strip().splitlines()
    max_vis = 0
    max_y, max_x = None, None
    for y in range(len(asteroid_map)):
        for x in range(len(asteroid_map[y])):
            vis = count_visible_asteroids(asteroid_map, y, x)
            if vis > max_vis:
                max_vis = vis
                max_y, max_x = y, x
    print(max_vis, max_y, max_x)
    special_y, special_x = lazer_asteroids(asteroid_map, max_y, max_x)
    return max_vis, special_x*100 + special_y


def main():
    # assert solve(example1)[0] == expected1
    part_one, part_two = solve(open("day10.input", "r").read())
    assert 269 == part_one
    print(part_two)


if __name__ == "__main__":
    main()
