from enum import Enum
from queue import Queue


def main():
    data1 = open("day15.input").read().strip().splitlines()
    print(run_simulation(data1))

    data2 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
    """.strip().splitlines()
    # print(run_simulation(data2))

    data3 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
    """.strip().splitlines()
    assert "47 * 590 = 27730" == run_simulation(data3)


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


class Goblin(Entity):
    @property
    def enemy_type(self):
        return Elf


class Elf(Entity):
    enemy_type = Goblin
    def __init__(self, x, y):
        super().__init__(x, y)
        self.attack_power = 20


def manhattan_distance(ent1, ent2):
    return abs(ent1.x - ent2.x) + abs(ent1.y - ent2.y)


def breadth_first_search(world, entity, goal_y, goal_x):
    visited = [[float("inf")] * len(row) for row in world]
    q = Queue()
    q.put((entity.y, entity.x, 0))
    while not q.empty():
        y, x, dist = q.get()
        if dist >= visited[y][x] or (
            world[y][x] != entity and world[y][x] != MapTile.OPEN.value
        ):
            continue
        visited[y][x] = dist
        if y == goal_y and x == goal_x:
            break

        for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            q.put((y + dy, x + dx, dist + 1))

    if visited[goal_y][goal_x] == float("inf"):
        return []

    y, x = goal_y, goal_x
    path = []
    while entity.y != y or entity.x != x:
        for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if visited[y][x] - 1 == visited[y + dy][x + dx]:
                path.append((y, x))
                y += dy
                x += dx
                break
    return path[::-1]


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


def run_simulation(lines):
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

    round_counter = 0
    while len(goblins) > 0 and len(elves) > 0:
        print("Round", round_counter)
        print_world(world)

        turn_order = sorted(elves + goblins, key=lambda e: (e.y, e.x))
        for entity in turn_order:
            if entity.hp <= 0:
                continue
            if type(entity) == Goblin:
                targets = elves
            else:
                targets = goblins

            attack_range = determine_attack_range(world, entity)
            if any([ar in targets for ar in attack_range]):
                # attack!
                fewest_hp = sorted(attack_range, key=lambda p: (p.hp, p.y, p.x))[0]
                fewest_hp.hp -= entity.attack_power
                elves, goblins = cleanup_dead_bodies(elves, world, goblins)
                continue

            in_range = []
            for t in targets:
                for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if world[t.y + dy][t.x + dx] == MapTile.OPEN.value:
                        in_range.append((t.y + dy, t.x + dx, t))

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

            if len(nearest) > 0 and min_distance > 0:
                # make move
                chosen = sorted(nearest, key=lambda p: (p[1], p[2]))[0]
                path = chosen[0]
                old_y, old_x = entity.y, entity.x
                new_y, new_x = path[0][0], path[0][1]
                entity.y = new_y
                entity.x = new_x
                world[old_y][old_x] = MapTile.OPEN.value
                world[new_y][new_x] = entity

            attack_range = determine_attack_range(world, entity)
            if any([ar in targets for ar in attack_range]):
                # attack!
                fewest_hp = sorted(attack_range, key=lambda p: (p.hp, p.y, p.x))[0]
                fewest_hp.hp -= entity.attack_power
                elves, goblins = cleanup_dead_bodies(elves, world, goblins)

        # all turns complete, time for the next round
        round_counter += 1

    print_world(world)
    hp_remaining = sum([e.hp for e in elves]) + sum([g.hp for g in goblins])
    outcome = round_counter * hp_remaining
    return f"{round_counter} * {hp_remaining} = {outcome}"


def determine_attack_range(world, entity):
    attack_range = [
        world[entity.y + 1][entity.x],
        world[entity.y][entity.x - 1],
        world[entity.y][entity.x + 1],
        world[entity.y - 1][entity.x],
    ]
    return [ar for ar in attack_range if type(ar) == entity.enemy_type]


def cleanup_dead_bodies(elves, world, goblins):
    for e in elves:
        if e.hp <= 0:
            world[e.y][e.x] = MapTile.OPEN.value
    for g in goblins:
        if g.hp <= 0:
            world[g.y][g.x] = MapTile.OPEN.value
    elves = [e for e in elves if e.hp > 0]
    goblins = [g for g in goblins if g.hp > 0]
    return elves, goblins


if __name__ == "__main__":
    main()
