from itertools import permutations
from intcode import run_program


def part_two(prog):
    program = list(map(int, prog.split(",")))
    phases = list(range(5, 10))
    max_thrust = float("-inf")
    for phase_perm in permutations(phases):
        loopback_thrust = 0
        def amp_a_input():
            yield phase_perm[0]
            while True:
                yield loopback_thrust
        def amp_b_input():
            yield phase_perm[1]
            for thrust in amp_a:
                yield thrust
        def amp_c_input():
            yield phase_perm[2]
            for thrust in amp_b:
                yield thrust
        def amp_d_input():
            yield phase_perm[3]
            for thrust in amp_c:
                yield thrust
        def amp_e_input():
            yield phase_perm[4]
            for thrust in amp_d:
                yield thrust

        amp_a = run_program(program.copy(), amp_a_input)
        amp_b = run_program(program.copy(), amp_b_input)
        amp_c = run_program(program.copy(), amp_c_input)
        amp_d = run_program(program.copy(), amp_d_input)
        amp_e = run_program(program.copy(), amp_e_input)
        for thrust in amp_e:
            loopback_thrust = thrust
            max_thrust = max(max_thrust, thrust)
    return max_thrust


def main():
    result = part_two("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5")
    print(result)
    assert 139629729 == result

    result = part_two(open("day7.input", "r").read())
    print(result)


if __name__ == "__main__":
    main()
