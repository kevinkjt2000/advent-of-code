from itertools import permutations
from intcode import run_program


def part_one(prog):
    program = list(map(int, prog.split(",")))
    outputs = list(run_program(program))
    return outputs


def main():
    assert [1125899906842624] == part_one("104,1125899906842624,99")

    assert [1219070632396864] == part_one("1102,34915192,34915192,7,4,7,99,0")

    assert [500] == part_one("109,2019,1101,200,300,1985,204,-34,99")

    assert ([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
            == part_one("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"))

    result = part_one(open("day9.input", "r").read())
    print(result)


if __name__ == "__main__":
    main()
