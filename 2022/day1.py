def gen_elves_from_file(filename="./2022/day1.input"):
    with open(filename, "r") as file_input:
        sum = 0
        for line in file_input.readlines():
            line = line.strip()
            if line == "":
                yield sum
                sum = 0
            else:
                sum += int(line)


def part1():
    elves = gen_elves_from_file()
    print(max(elves))


def part2():
    elves = sorted(gen_elves_from_file())
    print(sum(elves[-3:]))


def main():
    part2()


if __name__ == "__main__":
    main()
