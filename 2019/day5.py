from intcode import run_program


def main():
    real_input = list(map(int, open("day5.input").read().strip().split(",")))
    result = run_program(real_input)


if __name__ == "__main__":
    main()
