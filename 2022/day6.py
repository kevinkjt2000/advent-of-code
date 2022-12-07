from more_itertools import sliding_window


def parse_file(filename="./2022/day6.input"):
    with open(filename, "r") as file:
        return file.read().strip()


def is_starting_packet(packet):
    return sorted({c for c in packet}) == sorted(packet)


def part1():
    datastream = parse_file()
    for i, window in enumerate(sliding_window(datastream, 4)):
        if is_starting_packet(window):
            print(i + 4)
            return


def part2():
    datastream = parse_file()
    for i, window in enumerate(sliding_window(datastream, 14)):
        if is_starting_packet(window):
            print(i + 14)
            return


def main():
    assert not is_starting_packet("aaaa")
    assert is_starting_packet("abcd")
    part2()


if __name__ == "__main__":
    main()
