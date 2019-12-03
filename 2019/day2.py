from queue import Queue


def run_program(program):
    pc = 0
    while True:
        op = program[pc]
        if op == 1:
            a = program[program[pc+1]]
            b = program[program[pc+2]]
            program[program[pc+3]] = a + b
            pc += 4
        elif op == 2:
            a = program[program[pc+1]]
            b = program[program[pc+2]]
            program[program[pc+3]] = a * b
            pc += 4
        elif op == 99:
            break
    print(program)
    return program[0]


def main():
    run_program([1,9,10,3,2,3,11,0,99,30,40,50])

    for noun in range(100):
        for verb in range(100):
            real_input = list(map(int, open("day2.input").read().strip().split(",")))
            real_input[1] = noun
            real_input[2] = verb
            try:
                result = run_program(real_input)
                if result == 19690720:
                    answer = 100 * noun + verb
                    print(f"100 * noun + verb = {answer}")
                    return
            except IndexError:
                pass


main()
