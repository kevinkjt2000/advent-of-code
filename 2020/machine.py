from copy import deepcopy
import parsec as p


@p.generate
def parse_program():
    integer_arg = p.regex(r"[+-][0-9]+").parsecmap(int)
    expression = (
        ((p.string("nop") << p.space()) + integer_arg) |
        ((p.string("acc") << p.space()) + integer_arg) |
        ((p.string("jmp") << p.space()) + integer_arg)
    )
    return (yield p.many(expression << p.optional(p.string("\n"))))


class Machine():
    def __init__(self, filename):
        with open(filename, "r") as file_input:
            self.prog = parse_program.parse(file_input.read())
        self.pc = 0
        self.acc = 0

    def check_for_infinite(self):
        visited_addresses = set()
        while self.pc not in visited_addresses:
            visited_addresses.add(self.pc)
            instr, arg = self.prog[self.pc]
            if instr == "jmp":
                self.pc += arg
            elif instr == "acc":
                self.acc += arg
                self.pc += 1
            elif instr == "nop":
                self.pc += 1
        return self.acc

    def check_for_single_instruction_corruption(self):
        for i in range(len(self.prog)):
            m = deepcopy(self)
            instr, arg = m.prog[i]
            if instr == "nop":
                m.prog[i] = ("jmp", arg)
            elif instr == "jmp":
                m.prog[i] = ("nop", arg)
            try:
                acc = m.check_for_infinite()
            except IndexError:
                assert m.pc == len(m.prog)
                return m.acc
