from queue import Queue
import sys
from intcode import run_program

north = 1
south = 2
west = 3
east = 4

sc_wall = 0
sc_moved = 1
sc_goal = 2

def get_dy_dx(direction):
    if direction == north:
        return 1, 0
    if direction == south:
        return -1, 0
    if direction == west:
        return 0, -1
    if direction == east:
        return 0, 1

def solve(data):
    maze = {(0, 0): "."}
    visited = {(0, 0): 0}
    please_visit = set([(-1, 0), (1, 0), (0, 1), (0, -1)])
    status_codes = Queue()
    def movement_commands():
        y, x = 0, 0
        dist = 0
        last_sc = None
        while len(please_visit) > 0:
            print_maze(maze)
            if (y, x) in visited:
                if (y+1, x) not in visited:
                    y += 1
                    dist += 1
                    print("north")
                    yield north
                    last_sc = status_codes.get()
                elif (y-1, x) not in visited:
                    y -= 1
                    dist += 1
                    print("south")
                    yield south
                    last_sc = status_codes.get()
                elif (y, x+1) not in visited:
                    x += 1
                    dist += 1
                    print("east")
                    yield east
                    last_sc = status_codes.get()
                elif (y, x-1) not in visited:
                    x -= 1
                    dist += 1
                    print("west")
                    yield west
                    last_sc = status_codes.get()
                else:
                    for movement in [north, south, west, east]:
                        dy, dx = get_dy_dx(movement)
                        if (y+dy, x+dx) in visited and visited[(y+dy, x+dx)] == dist-1:
                            y += dy
                            x += dx
                            dist -= 1
                            print(f"backtracking {movement}")
                            yield movement
                            last_sc = status_codes.get()
                            break
                    continue
                for dy, dx in map(get_dy_dx, [north, south, west, east]):
                    if (y+dy, x+dx) not in visited:
                        please_visit.add((y+dy, x+dx))
            visited[(y, x)] = dist
            please_visit.remove((y, x))
            if last_sc == sc_wall:
                maze[(y, x)] = "#"
                for movement in [north, south, west, east]:
                    dy, dx = get_dy_dx(movement)
                    if (y+dy, x+dx) in visited and visited[(y+dy, x+dx)] == dist-1:
                        y += dy
                        x += dx
                        dist -= 1
                        break
            elif sc == sc_moved:
                maze[(y, x)] = "."
            elif sc == sc_goal:
                maze[(y, x)] = "G"
                print(f"goal at {(y, x)}")

    try:
        outputs = run_program(map(int, data.split(",")), movement_commands)
        for sc in outputs:
            status_codes.put(sc)
    finally:
        print(visited)
        maze[(0, 0)] = "S"
        print_maze(maze)


def print_maze(maze):
    min_x = min(x for _y, x in maze)
    prev_y = None
    prev_x = None
    for y, x in sorted(maze, key=lambda p: (-p[0], p[1])):
        if y != prev_y:
            print()
            sys.stdout.write(" " * abs(min_x - x))
            prev_y = y
            prev_x = x
        if x != prev_x + 1:
            sys.stdout.write(" " * (abs(prev_x - x) - 1))
        sys.stdout.write(maze[(y, x)])
        prev_x = x
    print()



def main():
    solve(open("day15.input").read())


if __name__ == "__main__":
    main()
