def default_input():
    while True:
        yield input()


def run_program(program, input_generator=default_input):
    program = {i: v for i, v in enumerate(program)}
    input_gen = input_generator()
    relative_base = 0
    def set_param(location, value, param_mode):
        if param_mode == 0:
            program[program.get(location, 0)] = value
        elif param_mode == 1:
            raise Exception("they said this would never happen")
        elif param_mode == 2:
            program[relative_base + program.get(location, 0)] = value
    def get_param(location, param_mode):
        if param_mode == 0:
            return program.get(program.get(location, 0), 0)
        elif param_mode == 1:
            return program.get(location, 0)
        elif param_mode == 2:
            return program.get(relative_base + program.get(location, 0), 0)
    pc = 0
    while True:
        op = program[pc] % 100
        param_mode_a = program[pc] // 100 % 10
        param_mode_b = program[pc] // 1000 % 10
        param_mode_c = program[pc] // 10000 % 10
        if op == 1:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            set_param(pc+3, a + b, param_mode_c)
            pc += 4
        elif op == 2:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            set_param(pc+3, a * b, param_mode_c)
            pc += 4
        elif op == 3:
            set_param(pc+1, int(next(input_gen)), param_mode_a)
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
            if a < b:
                set_param(pc+3, 1, param_mode_c)
            else:
                set_param(pc+3, 0, param_mode_c)
            pc += 4
        elif op == 8:
            a = get_param(pc+1, param_mode_a)
            b = get_param(pc+2, param_mode_b)
            if a == b:
                set_param(pc+3, 1, param_mode_c)
            else:
                set_param(pc+3, 0, param_mode_c)
            pc += 4
        elif op == 9:
            a = get_param(pc+1, param_mode_a)
            relative_base += a
            pc += 2
        elif op == 99:
            break
        else:
            print("Unrecognized op", op)
            break
