last = 894501

state = [3, 7]
recipes = 2
elves = list(range(0, 2))
while True:
    state_sum = [int(digit) for digit in
                 str(sum([state[elf] for elf in elves]))]
    for num in state_sum:
        state.append(num)
    for (e, elf) in enumerate(elves):
        elves[e] = (1 + elf + state[elf]) % len(state)
    try:
        number = "".join([str(digit) for digit in state]).index(str(last))
        print(number)
        break
    except ValueError:
        pass

# print(elves, state[-10:])
