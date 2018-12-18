data = """
################################
################.G#...##...#####
#######..#######..#.G..##..#####
#######....#####........##.#####
######.....#####.....GG.##.#####
######..GG.##.###G.........#####
#####........G####.......#######
######.#..G...####........######
##########....#####...G...######
########.......###..........####
#########...GG####............##
#########....................###
######........#####...E......###
####....G....#######........####
###.........#########.......####
#...#.G..G..#########..........#
#..###..#...#########E.E....E###
#..##...#...#########.E...E...##
#.....G.....#########.........##
#......G.G...#######........####
###..G...#....#####........#####
###########....G........EE..####
##########...................###
##########...................###
#######.............E....##E####
#######................#########
########.#.............#########
#######..#####.#......##########
######...#######...##.##########
################..###.##########
###############.......##########
################################
""".strip()

data2 = """
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
""".strip()

lines = data2.split("\n")

from enum import Enum

class MapTile(Enum):
    WALL = "#"
    OPEN = "."
    GOBLIN = "G"
    ELF = "E"

class Entity(object):
    def __init__(self, x, y):
        self.hp = 200
        self.attack_power = 3
        self.x = x
        self.y = y

    # def __repr__(self):
    #     return f"({self.hp})"

class Goblin(Entity):
    pass

class Elf(Entity):
    pass

def manhattan_distance(ent1, ent2):
    return abs(ent1.x - ent2.x) + abs(ent1.y - ent2.y)

goblins = []
elves = []
world = []
for (y, line) in enumerate(lines):
    world.append([None] * len(line))
    for (x, c) in enumerate(line):
        if c == MapTile.GOBLIN.value:
            world[y][x] = Goblin(x, y)
            goblins.append(world[y][x])
        elif c == MapTile.ELF.value:
            world[y][x] = Elf(x, y)
            elves.append(world[y][x])
        else:
            world[y][x] = c

def breadth_first_search(world, entity, goal_y, goal_x):
    from queue import Queue
    visited = [[(-1, -1, 0)] * len(row) for row in world]
    q = Queue()
    q.put((entity.y, entity.x))
    path = []
    while not q.empty():
        y, x = q.get()
        if y == goal_y and x == goal_x:
            py, px, _dist = visited[y][x]
            path = [(y, x), (py, px)]
            break

        for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            dist = visited[y][x][2] + 1
            if ((visited[y + dy][x + dx] == (-1, -1, 0) or dist < visited[y + dy][x + dx][2]) and
                    world[y + dy][x + dx] == MapTile.OPEN.value):
                q.put((y + dy, x + dx))
                visited[y + dy][x + dx] = (y, x, dist)

    if path == []:
        return []
    while path[-1] != (entity.y, entity.x):
        y, x = path[-1]
        ny, nx, _dist = visited[y][x]
        path.append((ny, nx))
    return path


def print_world(world):
    for row in world:
        healths = []
        for col in row:
            if type(col) == Goblin:
                healths.append(str(col.hp))
                col = "G"
            if type(col) == Elf:
                healths.append(str(col.hp))
                col = "E"
            print(col, end="")
        print(" ", " ".join(healths))
    print("")

round_counter = 0
print_world(world)
while len(goblins) > 0 and len(elves) > 0:
    turn_order = sorted(elves + goblins, key=lambda e: (e.y, e.x))
    for (i, entity) in enumerate(turn_order):
        if entity.hp <= 0:
            continue
        if type(entity) == Goblin:
            targets = elves
        else:
            targets = goblins

        attack_range = [
            world[entity.y+1][entity.x],
            world[entity.y][entity.x-1],
            world[entity.y][entity.x+1],
            world[entity.y-1][entity.x],
        ]
        attack_range = [ar for ar in attack_range if type(ar) in [Goblin, Elf]]
        if any([ar in targets for ar in attack_range]):
            # attack!
            fewest_hp = sorted(attack_range, key=lambda p: (p.hp, p.y, p.x))[0]
            fewest_hp.hp -= entity.attack_power
            # cleanup the dead bodies before the next turn
            for e in elves:
                if e.hp <= 0:
                    world[e.y][e.x] = MapTile.OPEN.value
            for g in goblins:
                if g.hp <= 0:
                    world[g.y][g.x] = MapTile.OPEN.value
            elves = [e for e in elves if e.hp > 0]
            goblins = [g for g in goblins if g.hp > 0]
            continue

        in_range = []
        for t in targets:
            if t.hp <= 0:
                continue
            # Check up, left, right, down (in that order)
            if world[t.y-1][t.x] == MapTile.OPEN.value:
                in_range.append((t.y-1, t.x, t))
            elif world[t.y][t.x-1] == MapTile.OPEN.value:
                in_range.append((t.y, t.x-1, t))
            elif world[t.y][t.x+1] == MapTile.OPEN.value:
                in_range.append((t.y, t.x+1, t))
            elif world[t.y+1][t.x] == MapTile.OPEN.value:
                in_range.append((t.y+1, t.x, t))

        reachable = []
        for point in in_range:
            path = breadth_first_search(world, entity, point[0], point[1])
            if len(path) > 0:
                reachable.append((path, point[0], point[1], point[2]))

        nearest = []
        if len(reachable) > 0:
            min_distance = len(min(reachable, key=lambda dist: len(dist[0]))[0])
            for point in reachable:
                if len(point[0]) == min_distance:
                    nearest.append(point)

        print(type(entity), entity.y, entity.x)
        if len(nearest) > 0 and min_distance > 1:
            # make move
            chosen = sorted(nearest, key=lambda p: (p[1], p[2]))[0]
            if type(entity) == Elf:
                print(nearest)
            if chosen:
                path = chosen[0]
                old_y, old_x = entity.y, entity.x
                new_y, new_x = path[-2][0], path[-2][1]
                entity.y = new_y
                entity.x = new_x
                world[old_y][old_x] = MapTile.OPEN.value
                world[new_y][new_x] = entity

    print_world(world)
    import pdb; pdb.set_trace()  # XXX BREAKPOINT

    # all turns complete, time for the next round
    round_counter += 1

hp_remaining = sum([e.hp for e in elves]) + sum([g.hp for g in goblins])
outcome = round_counter * hp_remaining
print(outcome)
