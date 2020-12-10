def read_input():
    with open("./day9.input", "r") as file_input:
        return list(map(int, file_input.readlines()))


def part1():
    numbers = read_input()
    print(find_weakness(numbers))


def part2():
    numbers = read_input()
    print(find_contiguous_weakness_sum(numbers))


def find_weakness(numbers):
    for i in range(25, len(numbers)):
        x = numbers[i]
        is_valid = False
        for j in range(i-25, i-1):
            y = numbers[j]
            for k in range(j+1, i):
                z = numbers[k]
                if x == y+z:
                    is_valid = True
                    break
            if is_valid:
                break
        if not is_valid:
            return x


def find_contiguous_weakness_sum(numbers):
    weakness = find_weakness(numbers)
    for i, x in enumerate(numbers):
        sum = x
        for j in range(i+1, len(numbers)):
            if sum == weakness:
                xs = numbers[i:j]
                return min(xs) + max(xs)
            sum += numbers[j]
            if sum > weakness:
                break


part2()
