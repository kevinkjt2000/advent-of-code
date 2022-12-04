def parse_file(filename="./2022/day2.input"):
    with open(filename, "r") as file_input:
        for line in file_input.readlines():
            yield line.strip().split(" ")


def score_strategy(strategy):
    points_for_choice = " XYZ".index(strategy[1])
    points_for_game_outcome = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        },
    }[strategy[0]][strategy[1]]
    return points_for_game_outcome + points_for_choice


def decide_shape_to_throw(strategy):
    return {
        "A": {
            "X": "Z",
            "Y": "X",
            "Z": "Y",
        },
        "B": {
            "X": "X",
            "Y": "Y",
            "Z": "Z",
        },
        "C": {
            "X": "Y",
            "Y": "Z",
            "Z": "X",
        },
    }[strategy[0]][strategy[1]]


def score_strategy_p2(strategy):
    shape = decide_shape_to_throw(strategy)
    return score_strategy([strategy[0], shape])


def tests():
    assert score_strategy(["A", "Y"]) == 8
    assert score_strategy_p2(["A", "Y"]) == 4


def part1():
    strategies = parse_file()
    scores = (score_strategy(s) for s in strategies)
    print(sum(scores))


def part2():
    strategies = parse_file()
    scores = (score_strategy_p2(s) for s in strategies)
    print(sum(scores))


def main():
    tests()
    part2()


if __name__ == "__main__":
    main()
