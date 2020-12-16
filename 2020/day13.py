from functools import reduce
from itertools import count, filterfalse, islice


def find_smallest_multiple_of_k_greater_than_or_equal_to_n(n, k):
    rem = (n + k) % k
    if rem == 0:
        return n
    else:
        return n + k - rem


def part1():
    with open("./day13.input") as file_input:
        lines = file_input.readlines()
        earliest_timestamp = int(lines[0])
        buses = [int(b) for b in lines[1].split(",") if b != "x"]
    best_bus = buses[0]
    best_timestamp = find_smallest_multiple_of_k_greater_than_or_equal_to_n(
        n=earliest_timestamp, k=best_bus
    )
    for b in buses:
        timestamp = find_smallest_multiple_of_k_greater_than_or_equal_to_n(
            n=earliest_timestamp, k=b
        )
        if timestamp < best_timestamp:
            best_timestamp = timestamp
            best_bus = b
    return best_bus * (best_timestamp - earliest_timestamp)


def find_next_overlap(bus1, bus2):
    t, dt = bus1
    i, b = bus2
    magic_numbers = list(
        islice(
            filterfalse(
                lambda _t: (_t + i) % b,
                count(t, dt),
            ),
            0,
            2,
        )
    )
    return (magic_numbers[0], magic_numbers[1] - magic_numbers[0])


def part2():
    with open("./day13.input") as file_input:
        lines = file_input.readlines()
        buses = [(i, int(b)) for (i, b) in enumerate(lines[1].split(",")) if b != "x"]

    t, _ = reduce(find_next_overlap, buses[1:], buses[0])
    return t


print(part2())
