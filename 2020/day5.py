def generate_row_col_values():
    with open("./day5.input") as file_input:
        for line in file_input.readlines():
            line = line.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
            row = int(line[0:7], 2)
            col = int(line[7:10], 2)
            yield row*8 + col


def part1():
    print(max(generate_row_col_values()))


def part2():
    pass


def main():
    part1()


if __name__ == "__main__":
    main()
