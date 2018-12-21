class Computer(object):
    NUM_REGISTERS = 6
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

    def set_ip_reg(self, ip_reg):
        self.ip_reg = ip_reg

    def __repr__(self):
        return f"{self.registers}"

    def run_program(self, program_lines):
        for i, line in enumerate(program_lines):
            inst, a, b, c = line.split(" ")
            program_lines[i] = (inst, int(a), int(b), int(c))

        ip = 0
        N = len(program_lines)
        prev = None
        while ip in range(N):
            self.registers[self.ip_reg] = ip
            inst, a, b, c = program_lines[ip]
            self.__getattribute__(inst)(a, b, c)
            ip = self.registers[self.ip_reg]
            ip += 1
            if ip == 25:
                print("lucky: ", self.registers)
            if prev != self.registers[0]:
                print(ip, self.registers)
            prev = self.registers[0]


if __name__ == "__main__":
    program = open("day19.input").read().strip()

    real_machine = Computer()
    # real_machine.registers[0] = 1
    program_lines = program.split("\n")
    ip_reg = int(program_lines.pop(0).split(" ")[1])
    real_machine.set_ip_reg(ip_reg)
    real_machine.run_program(program_lines)

    print(real_machine.registers[0])
