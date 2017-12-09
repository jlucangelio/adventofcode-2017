INSTRS = []

with open("day5.input") as f:
    INSTRS = [int(l.strip()) for l in f.readlines()]

# INSTRS = [0, 3,  0,  1,  -3]

pc = 0
steps = 0

while pc >= 0 and pc < len(INSTRS):
    offset = INSTRS[pc]
    if offset >= 3:
        INSTRS[pc] -= 1
    else:
        INSTRS[pc] += 1
    pc += offset
    steps += 1

print steps
