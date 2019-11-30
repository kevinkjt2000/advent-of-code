data = open("day16.input").read().strip()

samples, program = data.split("\n\n\n\n")
samples = samples.split("\n\n")


class Computer(object):
    NUM_REGISTERS = 4
    INSTRUCTIONS = [
        'addi', 'addr', 'andi', 'andr',
        'bori', 'borr', 'eqir', 'eqri',
        'eqrr', 'gtir', 'gtri', 'gtrr',
        'muli', 'mulr', 'seti', 'setr'
    ]

    def __init__(self, starting_values=[0] * NUM_REGISTERS):
        self.registers = starting_values

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def andr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def andi(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def setr(self, a, _b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, _b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        if a > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def gtri(self, a, b, c):
        if self.registers[a] > b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def gtrr(self, a, b, c):
        if self.registers[a] > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqir(self, a, b, c):
        if a == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqri(self, a, b, c):
        if self.registers[a] == b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def eqrr(self, a, b, c):
        if self.registers[a] == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def __repr__(self):
        return f"{self.registers}"


from copy import deepcopy
mappings = {}
op_code_mappings = {}
for (sample_id, s) in enumerate(samples):
    before, during, after = s.split("\n")
    starting_values = eval(before.split(": ")[1])
    op_code, a, b, c = [int(x) for x in during.split(" ")]
    expected_values = eval(after.split(": ")[1])
    for i in Computer.INSTRUCTIONS:
        machine = Computer(deepcopy(starting_values))
        machine.__getattribute__(i)(a, b, c)
        if machine.registers == expected_values:
            if sample_id not in mappings:
                mappings[sample_id] = []
            mappings[sample_id].append(i)

            if op_code not in op_code_mappings:
                op_code_mappings[op_code] = {i: 0 for i in Computer.INSTRUCTIONS}
            op_code_mappings[op_code][i] += 1

print(sum([1 for m in mappings if len(mappings[m]) >= 3]))

real_mappings = {}
while len(op_code_mappings) > 0:
    for op_code in op_code_mappings:
        non_zero_counts = [i for i in op_code_mappings[op_code]
                           if op_code_mappings[op_code][i] > 0]
        if len(non_zero_counts) == 1:
            real_mappings[op_code] = non_zero_counts[0]
            for m in op_code_mappings:
                op_code_mappings[m].pop(non_zero_counts[0])
            op_code_mappings.pop(op_code)
            break

real_machine = Computer()
program_lines = program.split("\n")
for line in program_lines:
    op_code, a, b, c = [int(x) for x in line.split(" ")]
    i = real_mappings[op_code]
    real_machine.__getattribute__(i)(a, b, c)

print(real_machine.registers[0])
