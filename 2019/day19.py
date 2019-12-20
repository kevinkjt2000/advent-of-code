import sys
from intcode import run_program

if __name__ == "__main__":

    scan = {}
    for y in range(50):
        for x in range(50):
            program = map(int, open("day19.input", "r").read().split(","))
            out = run_program(program, lambda: (i for i in (x, y)))
            scan[(y, x)] = next(out)

    for y in range(50):
        for x in range(50):
            sys.stdout.write(str(scan[(y,x)]))
        sys.stdout.write("\n")

    print(sum(scan.values()))
