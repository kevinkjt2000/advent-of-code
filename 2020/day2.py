import re


def part1():
    pattern = re.compile("[-: ]+")
    total_good = 0
    with open("./day2.input") as file_input:
        for line in file_input.readlines():
            minimum, maximum, letter, password = pattern.split(line)
            minimum = int(minimum)
            maximum = int(maximum)
            if password.count(letter) in range(minimum, maximum+1):
                total_good += 1
    print(total_good)


def part2():
    pattern = re.compile("[-: ]+")
    total_good = 0
    with open("./day2.input") as file_input:
        for line in file_input.readlines():
            i, j, letter, password = pattern.split(line)
            i = int(i)
            j = int(j)
            if (password[i-1] == letter) ^ (password[j-1] == letter):
                total_good += 1
    print(total_good)


def main():
    part2()


if __name__ == "__main__":
    main()
