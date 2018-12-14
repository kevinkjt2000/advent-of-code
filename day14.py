last = 894501

state = [3, 7]
recipes = 2
elves = list(range(0, 2))
while len(state) < last + 10:
    state_sum = [int(digit) for digit in
                 str(sum([state[elf] for elf in elves]))]
    for num in state_sum:
        state.append(num)
    for (e, elf) in enumerate(elves):
        elves[e] = (1 + elf + state[elf]) % len(state)

print(elves, state[-10:])
