from itertools import cycle, islice


def f(x, i):
    x = x // (i+1)
    if x % 2 == 0:
        return 0
    return (-1) ** ((x-1) // 2)


def pattern_generator(index):
    [0, 1, 0, -1]
    skip_first = True
    while True:
        patt = next(pattern_cycle)
        for i in range(0, index+1):
            if skip_first:
                skip_first = False
                continue
            yield patt


def main():
    input_list = list(map(int, open("day16.input", "r").read().strip()))
    # input_list = list(map(int, "03036732577212944063491565474664"))
    solve(input_list * 10000)


def solve(input_list):
    offset = int("".join(map(str, input_list[:7])))
    for phase in range(1, 101):
        output_list = input_list.copy()
        for i in range(len(input_list)):
            pg = pattern_generator(i)
            result = sum(input_digit * pattern_value for input_digit, pattern_value in zip(input_list, pg))
            output_list[i] = abs(result) % 10
        input_list = output_list.copy()
    print(input_list)
    print(offset)
    print(input_list[offset-1:offset+8])


if __name__ == "__main__":
    main()
