def default_input():
    while True:
        yield input()


def run_program(program, input_generator=default_input):
    input_gen = input_generator()
    def get_param(location, param_mode):
        if param_mode == 0:
            return program[program[location]]
        elif param_mode == 1:
            return program[location]
    pc = 0
    while True:
        op = program[pc] % 100
        param_mode_a = program[pc] // 100 % 10
        param_mode_b = program[pc] // 1000 % 10
        param_mode_c = program[pc] // 10000 % 10
        if op == 1:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            program[program[pc+3]] = a + b
            pc += 4
        elif op == 2:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            program[program[pc+3]] = a * b
            pc += 4
        elif op == 3:
            program[program[pc+1]] = int(next(input_gen))
            pc += 2
        elif op == 4:
            a = get_param(pc+1, param_mode_a)
            print(a)
            yield a
            pc += 2
        elif op == 5:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            if a != 0:
                pc = b
            else:
                pc += 3
        elif op == 6:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            if a == 0:
                pc = b
            else:
                pc += 3
        elif op == 7:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            c = program[pc+3]
            if a < b:
                program[c] = 1
            else:
                program[c] = 0
            pc += 4
        elif op == 8:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            c = program[pc+3]
            if a == b:
                program[c] = 1
            else:
                program[c] = 0
            pc += 4
        elif op == 99:
            break
        else:
            print("Unrecognized op", op)
            break
