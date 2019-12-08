import itertools


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def solve(data, width, height):
    data_iter = (d for d in data)
    min_zeros = float("inf")
    answer = None
    for layer in grouper(data_iter, width*height):
        layer = str(layer)
        num_zeros = layer.count("0")
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            answer = layer.count("1") * layer.count("2")
    return answer


def part_two(data, width, height):
    data_iter = (d for d in data)
    answer = ["2"] * (width * height)
    layers = list(grouper(data_iter, width*height))
    for layer in layers:
        layer = list(layer)
        for row in grouper(answer, width):
            print("".join(row))
        print()
        for i, pixel in enumerate(layer):
            if (pixel == "0" or pixel == "1") and answer[i] == "2":
                answer[i] = pixel
    for row in grouper(answer, width):
        print("".join(row).replace("0", " "))


def main():
    real_input = open("day8.input").read().strip()
    part_two(real_input, 25, 6)
    part_two("0222112222120000", 2, 2)


if __name__ == "__main__":
    main()
