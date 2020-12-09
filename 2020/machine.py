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
            last_known_acc = self.acc
            instr, arg = self.prog[self.pc]
            if instr == "jmp":
                self.pc += arg
            elif instr == "acc":
                self.acc += arg
                self.pc += 1
            elif instr == "nop":
                self.pc += 1
        return last_known_acc
