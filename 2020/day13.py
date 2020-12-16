from itertools import count, filterfalse, islice
from tqdm import tqdm


def find_smallest_multiple_of_k_greater_than_or_equal_to_n(n, k):
    rem = (n + k) % k
    if (rem == 0):
        return n
    else:
        return (n + k - rem)


def part1():
    with open("./day13.input") as file_input:
        lines = file_input.readlines()
        earliest_timestamp = int(lines[0])
        buses = [int(b) for b in lines[1].split(",") if b != "x"]
    best_bus = buses[0]
    best_timestamp = find_smallest_multiple_of_k_greater_than_or_equal_to_n(n=earliest_timestamp, k=best_bus)
    for b in buses:
        timestamp = find_smallest_multiple_of_k_greater_than_or_equal_to_n(n=earliest_timestamp, k=b)
        if timestamp < best_timestamp:
            best_timestamp = timestamp
            best_bus = b
    return best_bus * (best_timestamp - earliest_timestamp)


def part2():
    with open("./day13.input") as file_input:
        lines = file_input.readlines()
        buses = [(int(b), i) for (i, b) in enumerate(lines[1].split(",")) if b != "x"]
    pbar = tqdm()

    buses = sorted(buses, key=lambda btup: btup[0], reverse=True)
    print(buses)
    print(list(islice(filterfalse(lambda t: (t + buses[1][1]) % buses[1][0], count(buses[0][1], buses[0][0])), 0, 2)))
    return

    dt = 17429 # buses[0][0]
    t = 4147 # buses[-1][0]
    while True:
        pbar.update()
        cool = True
        for (b, i) in buses:
            if 0 != (t + i) % b:
                cool = False
                break
        if cool:
            pbar.close()
            return t
        t += dt


print(part2())
