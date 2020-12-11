def read_input():
    with open("./day10.input", "r") as file_input:
        adapters = list(map(int, file_input.readlines()))
    adapters.append(0)  # Have to account for the 0-rated outlet
    adapters.append(max(adapters) + 3)  # Device is rated 3 higher than the best adapter
    return sorted(adapters)


def part1():
    adapters = read_input()
    freq = {}
    for i in range(0, len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        if diff not in freq:
            freq[diff] = 0
        freq[diff] += 1
    return freq[1] * freq[3]


def part2():
    adapters = read_input()

    adapters_set = set(adapters)
    path_counts = {x: 0 for x in adapters}
    path_counts[0] = 1
    adapters.remove(0)
    for x in adapters:
        for y in range(x-3, x):
            if y in path_counts:
                path_counts[x] += path_counts[y]
    return path_counts[max(adapters)]


print(part2())
