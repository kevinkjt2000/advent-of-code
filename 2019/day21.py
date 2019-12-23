from itertools import product
import sys
from intcode import run_program

def jumpscript_guess(jumpscript):
    def f():
        for line in jumpscript:
            for ch in line:
                yield ord(ch)
            yield ord("\n")
        yield ord("W")
        yield ord("A")
        yield ord("L")
        yield ord("K")
        yield ord("\n")
    return f

if __name__ == "__main__":
    instructions = ["NOT", "AND", "OR"]
    xs = "ABCDJT"
    ys = ["J", "T"]
    program = list(map(int, open("day21.input", "r").read().split(",")))
    for length in range(16):
        print("length", length)
        possible_instructions = list(map(" ".join, product(instructions, xs, ys)) for i in range(length+1))
        for jumpscript in product(*possible_instructions):
            for i, o in enumerate(run_program(program.copy(), jumpscript_guess(jumpscript))):
                if o > 255:
                    print(jumpscript)
                    print(i)
                    print(o)
                    exit(0)
                if i > 40:
                    break
