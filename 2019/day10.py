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
    print(ay, ax)
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
            dy = y - ay
            dx = x - ax
            gcd = math.gcd(dy, dx)
            if gcd != 0:
                dy //= gcd
                dx //= gcd
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
                sys.stdout.write("1")
                num_visible += 1
            else:
                sys.stdout.write("0")
        sys.stdout.write(" ")
        print("".join(map(str, map(int, visible[y]))))
    print(num_visible)
    return num_visible


def solve(asteroid_map):
    asteroid_map = asteroid_map.strip().splitlines()
    max_vis = 0
    for y in range(len(asteroid_map)):
        for x in range(len(asteroid_map[y])):
            vis = count_visible_asteroids(asteroid_map, y, x)
            max_vis = max(vis, max_vis)
    print(max_vis)
    return max_vis


def main():
    assert solve(example1) == expected1
    solve(open("day10.input", "r").read())


if __name__ == "__main__":
    main()
