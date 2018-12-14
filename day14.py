import re
goal = "894501"
goal_regex = re.compile(goal)
goal_length = len(goal)

state = "37"
elves = list(range(0, 2))
start_search_at = 0 - goal_length
while True:
    state_sum = str(sum([int(state[elf]) for elf in elves]))
    state += state_sum
    for (e, elf) in enumerate(elves):
        elves[e] = (1 + elf + int(state[elf])) % len(state)

    match = goal_regex.search(state, start_search_at)
    if match:
        print(match.start())
        break
    start_search_at = len(state) - goal_length
