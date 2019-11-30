initial_state = "#...#..##.......####.#..###..#.##..########.#.#...#.#...###.#..###.###.#.#..#...#.#..##..#######.##"

generation_notes = """
##### => .
####. => #
###.# => #
###.. => #
##.## => #
##.#. => #
##..# => .
##... => #
#.### => .
#.##. => #
#.#.# => .
#.#.. => #
#..## => #
#..#. => #
#...# => .
#.... => .
.#### => #
.###. => .
.##.# => #
.##.. => #
.#.## => #
.#.#. => .
.#..# => #
.#... => .
..### => .
..##. => .
..#.# => #
..#.. => #
...## => .
...#. => #
....# => .
..... => .
""".strip().replace(".", "_").split("\n")

initial_state2 = "#..#.#..##......###...###"

generation_notes2 = """
##### => .
####. => #
###.# => #
###.. => #
##.## => #
##.#. => #
##..# => .
##... => .
#.### => #
#.##. => .
#.#.# => #
#.#.. => .
#..## => .
#..#. => .
#...# => .
#.... => .
.#### => #
.###. => .
.##.# => .
.##.. => #
.#.## => #
.#.#. => #
.#..# => .
.#... => #
..### => .
..##. => .
..#.# => .
..#.. => #
...## => #
...#. => .
....# => .
..... => .
""".strip().replace(".", "_").split("\n")

import re
state = initial_state.replace(".", "_")
index = 0
gen = 0
prev_total = 0
index_copy = index
for plant in state:
    if plant == "#":
        prev_total += index_copy
    index_copy += 1
prev_diffs = [None] * 5
# print(gen, state)
for _ in range(0, 1000):
    locations = []
    while "#" in state[:3]:
        state = "_" + state
        index -= 1
    while "#" in state[-3:]:
        state += "_"
    for note in generation_notes:
        pattern, replacement = note.split(" => ")
        for m in re.finditer(f"(?={pattern})", state):
            locations.append((m.start()+2, replacement))
    for (loc,pot) in locations:
        state = state[:loc] + pot + state[loc+1:]
    gen += 1

    total = 0
    index_copy = index
    for plant in state:
        if plant == "#":
            total += index_copy
        index_copy += 1
    print(total)
    prev_diffs.append(total - prev_total)
    prev_total = total
    prev_diffs.pop(0)
    if all(map(lambda tot: tot == prev_diffs[0], prev_diffs)):
        print(gen, "here!", total)
        print(total + prev_diffs[0] * (50_000_000_000 - gen))
        break

