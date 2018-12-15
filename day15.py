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

lines = data.split("\n")

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

    def __repr__(self):
        return f"({self.hp})"

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

# TODO implement these three/collapse them into one
def path_distance(world, entity, y, x):
    return 0

def is_path_possible(world, entity, y, x):
    return True

def move_entity_towards_chosen(world, entity, y, x):
    pass

round_counter = 0
while len(goblins) > 0 and len(elves) > 0:
    turn_order = sorted(elves + goblins, key=lambda e: (e.y, e.x))
    for (i, entity) in enumerate(turn_order):
        if entity.hp <= 0:
            continue
        if type(entity) == Goblin:
            targets = elves
        else:
            targets = goblins

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
            if is_path_possible(world, entity, point[0], point[1]):
                reachable.append(point)

        distances = []
        for point in reachable:
            distances.append((
                path_distance(world, entity, point[0], point[1]),
                point[0],
                point[1],
                point[2]
            ))

        min_distance = min(distances, key=lambda dist: dist[0])
        nearest = []
        for point in distances:
            if point[0] == min_distance:
                nearest.append(point)

        chosen = None
        if len(nearest) > 0:
            if min_distance > 0:
                # make move
                chosen = sorted(nearest, key=lambda p: (p[1], p[2]))[0]
                if chosen:
                    move_entity_towards_chosen(world, entity, chosen[1], chosen[2])
            else:
                # attack!
                chosen = sorted(nearest, key=lambda p: (p[3].hp, p[1], p[2]))[0]
                chosen[3].hp -= entity.attack_power

        # cleanup the dead bodies before the next turn
        for e in elves:
            if e.hp <= 0:
                world[e.y][e.x] = MapTile.OPEN
        for g in goblins:
            if g.hp <= 0:
                world[g.y][g.x] = MapTile.OPEN
        elves = [e for e in elves if e.hp > 0]
        goblins = [g for g in goblins if g.hp > 0]

    # all turns complete, time for the next round
    round_counter += 1

hp_remaining = sum([e.hp for e in elves]) + sum([g.hp for g in goblins])
outcome = round_counter * hp_remaining
print(outcome)
