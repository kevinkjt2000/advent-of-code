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
    asteroid_locations = get_other_asteroids(asteroid_map, ay, ax)
    slope_groups = get_slope_groups(asteroid_locations, ay, ax)

    visible = {(y, x): True for y, x in asteroid_locations}
    for slope in slope_groups:
        for asteroid in slope_groups[slope][1:]:
            visible[asteroid] = False

    num_visible = 0
    for asteroid in visible:
        if visible[asteroid]:
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
    asteroid_locations = get_other_asteroids(asteroid_map, sy, sx)
    slope_groups = get_slope_groups(asteroid_locations, sy, sx)

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
            lazered_so_far += 1
        if lazered_so_far == 200:
            return (y, x)

def get_slope_groups(asteroid_locations, sy, sx):
    slope_groups = {}
    for y, x in asteroid_locations:
        dy, dx = calc_slope(y, x, sy, sx)
        if (dy, dx) not in slope_groups:
            slope_groups[(dy, dx)] = []
        slope_groups[(dy, dx)].append((y, x))
    # sort slope groups by distance from stationed lazer base
    for sg in slope_groups:
        slope_groups[sg].sort(key=lambda p: calc_distance((sy, sx), p), reverse=True)
    return slope_groups

def get_other_asteroids(asteroid_map, sy, sx):
    asteroid_locations = []
    for y, row in enumerate(asteroid_map):
        for x, col in enumerate(row):
            if asteroid_map[y][x] == "#" and (y != sy or x != sx):
                asteroid_locations.append((y, x))
    return asteroid_locations


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
