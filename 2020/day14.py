def apply_mask(mask, value):
    p = int(mask.replace("1", "0").replace("X", "1"), 2)
    q = int(mask.replace("X", "0"), 2)
    return value & p | q


assert apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11) == 73
assert apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101) == 101
assert apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 0) == 64


memory = {}
mask = None
for line in open("./day14.input", "r").readlines():
    directive, value = line.split(" = ")
    if directive == "mask":
        mask = value
    else:
        address = int(directive.replace("mem[", "").replace("]", ""))
        masked_value = apply_mask(mask, int(value))
        memory[address] = masked_value

print(sum(memory[addr] for addr in memory))
