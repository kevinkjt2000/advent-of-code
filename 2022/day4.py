import re


def parse_file(filename="./2022/day4.input"):
    r = re.compile("[,-]")
    with open(filename, "r") as file_input:
        for line in file_input.readlines():
            yield [int(i) for i in r.split(line.strip())]


def part1():
    count = 0
    for ns in parse_file():
        a, b, c, d = ns
        if c <= a and b <= d or (a <= c and d <= b):
            count += 1
    print(count)


def part2():
    count = 0
    for ns in parse_file():
        a, b, c, d = ns
        if (
            a in range(c, d + 1)
            or b in range(c, d + 1)
            or c in range(a, b + 1)
            or d in range(a, b + 1)
        ):
            count += 1
    print(count)


def main():
    part2()


if __name__ == "__main__":
    main()
