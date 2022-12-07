import numpy
import re


def parse_file(filename="./2022/day5.input"):
    with open(filename, "r") as file_input:
        lines = file_input.read().splitlines()
    stack_lines = [[c for c in l] for l in lines[0:8]]
    transposed_stack_lines = ["".join(s).strip() for s in numpy.transpose(stack_lines)]
    stacks = [
        s for s in transposed_stack_lines if "[" not in s and "]" not in s and s != ""
    ]

    r = re.compile(r"[0-9]+")
    instructions = [[int(x) for x in r.findall(l)] for l in lines[10:]]
    return stacks, instructions


def part1():
    stacks, instructions = parse_file()
    for instruction in instructions:
        count, source, dest = instruction
        source -= 1
        dest -= 1
        stacks[dest] = stacks[source][0:count][::-1] + stacks[dest]
        stacks[source] = stacks[source][count:]
    print("".join(s[0] for s in stacks))


def part2():
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
