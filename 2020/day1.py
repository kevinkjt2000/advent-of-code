def part1():
    encountered = set()
    with open("./day1.input") as file_input:
        for line in file_input.readlines():
            num = int(line)
            counterpart = 2020 - num
            if counterpart in encountered:
                print(num * counterpart)
                break
            else:
                encountered.add(num)


def part2():
    numbers = []
    with open("./day1.input") as file_input:
        for line in file_input.readlines():
            num = int(line)
            numbers.append(num)
    n = len(numbers)
    numbers = sorted(numbers)
    lookup_set = set(numbers)
    minimum = numbers[0]
    for i in range(0, n-2):
        x = numbers[i]
        for j in range(i+1, n-1):
            y = numbers[j]
            if x + y + minimum > 2020:
                break
            z = 2020 - x - y
            if z in lookup_set:
                print(x * y * z)
                return


def main():
    part2()


if __name__ == "__main__":
    main()
