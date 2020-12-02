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
    for i in range(0, n-2):
        x = numbers[i]
        for j in range(i+1, n-1):
            y = numbers[j]
            if x + y > 2020:
                break
            for k in range(j+1, n):
                z = numbers[k]
                total = x + y + z
                if total == 2020:
                    print(x * y * z)
                    return
                if total > 2020:
                    break


def main():
    part2()


if __name__ == "__main__":
    main()
