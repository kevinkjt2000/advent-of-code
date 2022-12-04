def parse_file(filename="./2022/day3.input"):
    with open(filename, "r") as file_input:
        for line in file_input.readlines():
            yield line.strip()


def get_item_priority(letter):
    alpha = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alpha.index(letter)


def tests():
    assert get_item_priority("a") == 1
    assert get_item_priority("Z") == 52


def part1():
    sacks = parse_file()
    total = 0
    for sack in sacks:
        compartment1 = {c for c in sack[: len(sack) // 2]}
        compartment2 = {c for c in sack[len(sack) // 2 :]}
        intersection = compartment1.intersection(compartment2)
        total += sum(get_item_priority(l) for l in intersection)
    print(total)


def part2():
    sacks = parse_file()
    total = 0
    try:
        while True:
            sack1 = {c for c in next(sacks)}
            sack2 = {c for c in next(sacks)}
            sack3 = {c for c in next(sacks)}
            intersection = sack1.intersection(sack2).intersection(sack3)
            total += sum(get_item_priority(l) for l in intersection)
    except StopIteration:
        pass
    print(total)


def main():
    tests()
    part2()


if __name__ == "__main__":
    main()
