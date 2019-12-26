import sys
from intcode import run_program, ascii_input


commands = """south
east
take whirled peas
west
north
north
west
west
take candy cane
west
west
take tambourine
east
east
east
east
east
take ornament
west
west
north
take astrolabe
east
take hologram
east
take klein bottle
west
west
south
east
east
north
north
take dark matter
south
south
west
west
north
east
south
west
drop ornament
drop klein bottle
drop dark matter
drop candy cane
drop hologram
drop astrolabe
drop whirled peas
drop tambourine
take astrolabe
take tambourine
take hologram
take klein bottle
north
"""


def semi_auto_input():
    for command in commands.splitlines():
        print(command)
        yield from map(ord, command)
        yield ord("\n")
    while True:
        yield from map(ord, input())
        yield ord("\n")


if __name__ == "__main__":
    program = map(int, open("day25.input", "r").read().split(","))
    for o in run_program(program, semi_auto_input):
        sys.stdout.write(chr(o))
