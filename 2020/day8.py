from machine import Machine

m = Machine("./day8.input")

def part1():
    print(m.check_for_infinite())

def part2():
    print(m.check_for_single_instruction_corruption())

part2()
